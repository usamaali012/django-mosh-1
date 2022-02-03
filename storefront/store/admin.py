from django.contrib import admin, messages 
from . import models
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.db.models.aggregates import Count

# Register your models here.
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'invetory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
            ]
    
    def queryset(self, request, queryset):
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10) 


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }
    
    autocomplete_fields = ['collection']
    actions = ['clear_inventory']
    search_fields = ['title']
    
    list_display = ['title', 'unit_price', 'inventory_status', 'collection']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]     
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    @admin.action(description="Clear inventory")
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.',
            messages.SUCCESS
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    list_per_page = 10
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']


    @admin.display(ordering='orders_count')
    def orders(self, customer):
        url = (
            reverse('admin:store_order_changelist')
            + '?'
            + urlencode({
                'customer__id': customer.id
            }))
        return format_html('<a href="{}">{} Orders</a>', url, customer.orders_count)

    def get_queryset(self, request): 
        return super().get_queryset(request).annotate(
            orders_count=Count('order')
        )


class OrderItemInLine(admin.StackedInline):
    model = models.OrderItem
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInLine]
    list_display = ['id', 'placed_at', 'customer']


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'products_count']

    @admin.display(ordering='products_count')
    def products_count(self, collection): 
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': collection.id
            })
            )

        return format_html('<a href="{}">{}</a>', url, collection.products_count)
        

    def get_queryset(self, request): 
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )



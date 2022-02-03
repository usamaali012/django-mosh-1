from django.contrib import admin

from store.models import Product
from store.admin import ProductAdmin
from tags.models import TaggedItem

from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

class TagInLine(GenericTabularInline):
    autocomplete_fields = ['tag']
    model  = TaggedItem


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInLine]

# As now we are going to register a new Product Model admin class because we have a new admin class for product
#  "CustomProductAdmin"
# We first have to unregister tho old Product Model.
admin.site.unregister(Product)                        
admin.site.register(Product, CustomProductAdmin)                     # Registering again with new admin class. 

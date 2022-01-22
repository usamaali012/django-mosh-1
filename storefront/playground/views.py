from django.shortcuts import render

from store.models import Collection, Customer, Product, OrderItem, Order 
from tags.models import TaggedItem

from django.db import transaction
from django.db import connection
from django.db.models.functions import Concat
from django.db.models import Value, Q, F, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Max, Min, Sum, Avg, Count

from django.contrib.contenttypes.models import ContentType

# Create your views here.


def sayHello(request):
    # query_set = Product.objects.all()
    
    # for product in query_set:
    #     print(product)

    # product = Product.objects.get(id=1)

    # product = Product.objects.get(pk=1)

    # products = list(query_set)

    # product_1 = query_set[0]
    
    # product_1_5 = query_set[0:5]

    ## Handling Exception:
    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     ...

    # product = Product.objects.filter(pk=0).first()

    # product = Product.objects.filter(pk=0).exists()

    # query_set = Product.objects.filter(unit_price__gt=20)

    # query_set = Product.objects.filter(unit_price__range=(20, 30))

    # query_set = Product.objects.filter(collection__id=1)

    # query_set = Product.objects.filter(collection__id=1)

    # query_set = Product.objects.filter(title__icontains='coffee')

    # query_set = Product.objects.filter(last_update__year=2021)

    # query_set = Product.objects.filter(description__isnull=True)

    # query_set = Product.objects.filter(inventory__lt=10) .filter(unit_price__lt=20)

    # query_set = Product.objects.filter(Q(inventory__lt=10) | Q(unit_price__lt=20))

    # query_set = Product.objects.filter(Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    # query_set = Product.objects.filter(inventory=F('unit_price'))

    # query_set = Product.objects.filter(inventory=F('collection__id'))

    # query_set = Product.objects.order_by('title')

    # query_set = Product.objects.order_by('-title')

    # query_set = Product.objects.order_by('unit_price', '-title')

    # product = Product.objects.order_by('unit_price')

    # product = Product.objects.earliest('unit_price')

    # product = Product.objects.latest('unit_price')

    # query_set = Product.objects.all()[:5]

    # query_set = Product.objects.all()[5:10]

    # queryset = Product.objects.values('id', 'title')

    # query_set = Product.objects.values('id', 'title', 'collection__title')

    # queryset = Product.objects.values_list('id', 'title', 'collection__title')

    # query_set = Product.objects.filter(id=F('orderitem__product_id')).order_by('title')

    # query_set = OrderItem.objects.values('product__id')

    # ordered_items = OrderItem.objects.values('product__id').distinct()
    # query_set = Product.objects.filter(id__in=ordered_items).order_by('title')

    # queryset = Product.objects.only('id', 'title')

    # queryset = Product.objects.defer('description')

    # queryset = Product.objects.all()

    # queryset = Product.objects.select_related('collection').all()

    # queryset = Product.objects.prefetch_related('promotions').all()

    # queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()

    # queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]

    # result = Product.objects.filter(collection__id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))

    # queryset = Customer.objects.annotate(is_new=Value(True))

    # queryset = Customer.objects.annotate(new_id=F('id'))

    # queryset = Customer.objects.annotate(new_id=F('id') + 1)

    # queryset = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))

    # queryset = Customer.objects.annotate(full_name=Concat('first_name', Value(' '), 'last_name'))

    # queryset = Customer.objects.annotate(orders_count=Count('order'))

    # queryset = Product.objects.annotate(discounted_price=F('unit_price') * 0.8)

    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    # queryset = Product.objects.annotate(discounted_price=discounted_price)

    # content_type = ContentType.objects.get_for_model(Product)
    # queryset = TaggedItem.objects.select_related('tag').filter(
        # content_type=content_type,
        # object_id=1
    # )
    # TaggedItem.objects.get_tags_for(Product, 1)

    # queryset = Product.objects.all()

    # queryset[0]

    # list(queryset)

    #CREATING OBJECTS:
    # collection = Collection(title='a')
    # collection.title = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # # collection.featured_product_id = 1
    # collection.save()
    # OR
    # Collection.objects.create(title='a', featured_prodcut_id=1)


    # UPDATING OBJECTS (#1) to update all the fields
    # collection = Collection(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()

    # UPDATING OBJECTS (#2) to update single or few fields
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = Product(pk=2)
    # collection.save()


    # UPDATING OBJECTS (#3)
    # Collection.objects.filter(pk=11).update(featured_product=None)




    # DELETING OBJECTS: (Single)
    # collection = Collection(pk=11)
    # collection.delete()


    # DELETING OBJECTS: (Multiple)
    # Collection.objects.filter(id__gt=5).delete()


    # Running multiple changes to database together:
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = -1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()


    # queryset = Product.objects.raw('SELECT * FROM store_product')

    # cursor = connection.cursor()
    # cursor.execute('SELECT * FROM store_product')
    # cursor.close()

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM store_product')    # cursor will close itself.

    return render(request, 'hello.html', {'name': 'Usama Ali ', 'results': ''})

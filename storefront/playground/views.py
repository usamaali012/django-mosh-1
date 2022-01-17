import collections
from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, OrderItem

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

    # query_set = Product.objects.values('id', 'title')

    # query_set = Product.objects.values('id', 'title', 'collection__title')

    # query_set = Product.objects.values_list('id', 'title', 'collection__title')

    # query_set = Product.objects.filter(id=F('orderitem__product_id')).order_by('title')

    # query_set = OrderItem.objects.values('product__id')

    ordered_items = OrderItem.objects.values('product__id').distinct()
    query_set = Product.objects.filter(id__in=ordered_items).order_by('title')

    print(query_set.count())

    return render(request, 'hello.html', {'name': '', 'products': list(query_set)})

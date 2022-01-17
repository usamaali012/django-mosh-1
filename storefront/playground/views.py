import collections
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product

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

    query_set = Product.objects.filter(description__isnull=True)

    return render(request, 'hello.html', {'name': '', 'products': list(query_set)})

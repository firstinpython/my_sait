from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.
def get_params(params, products):
    fbrand = {}
    for product in products:
        fbrand[product.brand.name] = product.brand.name
    dict_params = {
        "sort": {
            "priceup": "-price",
            "pricedown": "price"
        },
        "fdlvt": {
            "24": 1,
            "48": 2,
            "72": 3
        },
        "fbrand": fbrand
    }
    for key, value in params.items():
        print(key)
        if key == "sort":
            if value in [v for v in dict_params[key]]:
                products = products.order_by(dict_params[key][value])
        if key == "fdlvt":
            if value in [v for v in dict_params[key]]:
                products = products.filter(delivery_time__lte=dict_params[key][value])
        if key == "fbrand":
            if value in [v for v in dict_params[key]]:
                products = products.filter(brand__name=dict_params[key][value])

    return products


def products_view(requests):
    products = Product.objects.all()
    params: dict = requests.GET
    products_f = get_params(params, products)
    print(products_f)
    return HttpResponse("ok")

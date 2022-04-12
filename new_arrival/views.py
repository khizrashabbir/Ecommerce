from django.shortcuts import render
from main.models import *


# Create your views here.
def arrival(request):
    context = {}
    try:
        context["categories"] = Category.objects.all()
        context["all_products"] = Product.objects.all()
    except Exception as e:
        print(e)
    return render(request, "new_arrival/product.html", context)


def filter_product_ajax_tab(request, id):
    context = {}
    try:
        context["tablet"] = Product.objects.filter(category__category_name='Tablet', category_id=id)
    except Exception as e:
        print(e)
    return render(request, "new_arrival/product_filter_phone.html", context)


def filter_product_ajax_tab(request):
    context = {}
    try:
        context["tablet"] = Product.objects.filter(category__category_name='Tablet')
    except Exception as e:
        print(e)
    return render(request, "new_arrival/product_filter_phone.html", context)


def filter_product_ajax_tab(request):
    context = {}
    try:
        context["tablet"] = Product.objects.filter(category__category_name='Tablet')
    except Exception as e:
        print(e)
    return render(request, "new_arrival/product_filter_phone.html", context)

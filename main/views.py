from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    context = {}
    try:
        # trending_objs = Product.objects.all()[:6]
        context['trending_items'] = Product.objects.filter(is_trending=True)
        context['companies'] = Company.objects.all()
        context['phone'] = Product.objects.filter(category__category_name='Phone')[:6]
        context['tablet'] = Product.objects.filter(category__category_name='Tablet')[:6]

    except Exception as e:
        print(e)
    return render(request, "main/index.html", context)


# for phone
def list_view(request, id):
    context = {}
    try:
        context["dataset"] = Product.objects.filter(company_id=id)
    except Exception as e:
        print(e)
    return render(request, "main/show_product_comapny.html", context)


# for tablets
def list_vieww(request, id):
    context={}
    try:
        context["dataset2"] = Product.objects.filter(company_id=id)
    except Exception as e:
        print(e)
    return render(request, "main/show_tab_comapny.html", context)


def filter_product_ajax(request, id):
    context = {}
    try:
        context["phone"] = Product.objects.filter(company_id=id, category__category_name='Phone')
    except Exception as e:
        print(e)
    return render(request, "main/filter_phone_product.html", context)


def filter_product_ajax_tab(request, id):
    context = {}
    try:
        context["tablet"] = Product.objects.filter(company_id=id, category__category_name='Tablet')
    except Exception as e:
        print(e)
    return render(request, "main/filter_tab_product.html", context)
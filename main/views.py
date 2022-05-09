from django.shortcuts import render, redirect
from .models import *
from .forms import ReviewForm
from users.views import login_request
from django.db.models import Sum
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='/login/')
def home(request):
    context = {}
    try:
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
    context = {}
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


def productDetail(request, id):
    context = {}
    try:
        if request.user.is_authenticated:
            if request.method == 'POST':
                productsa = Product.objects.get(id=id)
                form = ReviewForm(request.POST)
                if form.is_valid():
                    forms = form.save(commit=False)
                    forms.product = productsa
                    forms.user = request.user
                    forms.save()
                return redirect("main:product_detail", id)
        form = ReviewForm()
        context['forms'] = form
        context["review"] = Review.objects.all()
        context["in_products"] = Product.objects.all()[:6]
        context["product"] = Product.objects.get(id=id)
        context["product_specification"] = ProductDescription.objects.get(id=id)
        context["table_components"] = AdditionalInfo.objects.all()
    except Exception as e:
        print(e)
    return render(request, "main/product_detail.html", context)


def cart_page(request, id):
    context = {}
    try:
        product = Product.objects.get(id=id)
        if request.method == 'POST':
            cart = AddCart.objects.filter(user=request.user, product_id=id).first()
            if cart:

                cart.quantity += 1
            else:
                cart = AddCart.objects.create(
                    product=product,
                    quantity=1,
                    user=request.user,
                )
            cart.save()

        context["product_cart"] = AddCart.objects.filter(user=request.user)

    except Exception as e:
        print(e)
    return render(request, "main/checkout_cart.html", context)
    # try:
    #     cart_item = AddCart.objects.get(product=product, cart=cart)
    #     if cart_item.quantity < cart_item.product.stock:
    #         cart_item.quantity += 1
    #     cart_item.save()

# cart = AddCart.objects.get(id=id)
# context["product_cart"] = Product.objects.get(id=id).annotate(Sum('price'))
# context["product_cart"] = Product.objects.get(id=id).aggregate(Sum('price'))
# context["product_cart"] = Product.objects.get(id=id)
# AddCart.objects.all()
# AddCart.objects.all().values()
# a.save()
# context["pro_enter"]= Product.objects.filter(id=id)
# if not Product in cart.Product.get(id=id):
#     cart.products_list.add(Product)
# else:
#     cart.products_list.remove(Product)
#     return HttpResponseRedirect("cart")
# cart_item = AddCart.objects.filter(user=request.user, product_id=id)
# id = []
# for item in cart:
#     id.append(item.id)
# AddCart.objects.create(user=request.user, product=product, quantity=1, price=product.off_price, single_total=product.off_price)
# AddCart.objects.save()

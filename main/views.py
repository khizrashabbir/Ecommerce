from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from . import forms
from .forms import ReviewForm


# Create your views here.
@login_required(login_url='/login/')
def home(request):
    context = {}
    try:
        # context[trending_objs] = Product.objects.all()[:6]
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


# product detail page

def productDetail(request, id):
    context = {}
    try:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect("main:product_detail", id)

        form = ReviewForm
        context['forms'] = form
        context["review"] = Review.objects.all()
        context["in_products"] = Product.objects.all()[:6]
        context["product"] = Product.objects.get(id=id)
        context["product_specification"] = ProductDescription.objects.get(id=id)
        context["table_components"] = AdditionalInfo.objects.all()

        # context["product_specification"] = ProductDescription.objects.get(id = Product.id, product__category_id=id)
        # context["product_specification"] = ProductDescription.objects.filter(id =ProductDescription.id)
        # context["product_specification"] = ProductDescription.objects.all()
        # context["product_specification"]= ProductDescription.objects.get(Product, id=id)
        # context["product_specification"] = ProductDescription.objects.filter(id)

    except Exception as e:
        print(e)
    return render(request, "main/product_detail.html", context)

# def add_review(request, id):
#     if request.user.is_authenticated:
#         review = Review.objects.get(id=id)
#         if request.method == "POST":
#             form = ReviewForm(request.POST or None)
#             if form.is_valid():
#                 data = form.save(commit=False)
#                 data.comment = request.POST["comment"]
#                 data.rating = request.POST["rating"]
#                 data.user = request.user
#                 data.review = review
#                 data.save()
#                 return redirect("main:product_detail", id)
#         else:
#             form = ReviewForm()
#         return render(request, "main/product_detail.html", {"form": form})
#
#     # def add_review(request, id):
#     #     post = Movie.objects.get(id=id)
#     #     form = ReviewForm(request.POST or None)
#     #     if form.is_valid():
#     #         author = request.POST.get('author')
#     #         stars = request.POST.get('stars')
#     #         comment = request.POST.get('comment')
#     #         review = Review(author=author, stars=stars, comment=comment, movie=post)
#     #         review.save()
#     #         return redirect('success')
#     #
#     #     form = ReviewForm()
#     #     context = {
#     #         "form": form
#     #
#     #     }
#     #     return render(request, 'main/product_detail.html', context)

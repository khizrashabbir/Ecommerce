from django.urls import path
from .views import *
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('list-view/<int:id>', views.list_view, name='list_view'),
    path('list-view/<int:id>', views.list_vieww, name='list_vieww'),
    path('filter-prodcuts/<int:id>', views.filter_product_ajax, name='filter_product'),
    path('filter-tab/<int:id>', views.filter_product_ajax_tab, name='filter_tab'),
    # product detail page
    path('product-detail/<int:id>/', views.productDetail, name="product_detail"),
    #     review page
    # path('addreview/<int:id>', views.add_review, name="add_review"),
]

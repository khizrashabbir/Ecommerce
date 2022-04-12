from . import views
from django.urls import path

urlpatterns = [
    path('arrival/', views.arrival, name="arrival"),

]
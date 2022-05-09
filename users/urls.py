from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.signup, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

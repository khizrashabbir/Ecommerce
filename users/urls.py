from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('login/', user_view.Login, name='login'),
    # path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
    path('home/', views.home, name = 'home'),
    path('register/', views.signup, name='register'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_view, name='logout')


]
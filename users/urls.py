from django.urls import path
# from user import views as user_view
from django.contrib.auth import views as auth
from . import views

urlpatterns = [
    # path('login/', user_view.Login, name='login'),
    # path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
    path('register/', views.signup, name='register'),
    path('login/', views.login_request, name='login'),

]
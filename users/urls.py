from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import redirect_home
from users import views as user_views

urlpatterns = [
  path('register/', user_views.register, name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
  path('profile/', redirect_home),
]
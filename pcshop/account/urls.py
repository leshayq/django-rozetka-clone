from django.urls import path
from django.shortcuts import render
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.logout_user, name='logout'),
    path('logout/', views.login_user, name='login'),
    path('email_verification/', views.email_verification, name='email_verification'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

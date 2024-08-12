from django.urls import path
from django.shortcuts import render
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.login_user, name='login'),
    path('email_verification/', views.email_verification, name='email_verification'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('account_delete/', views.delete_user, name='account_delete'),
    path('account_update/', views.profile_user, name='account_update'),
]

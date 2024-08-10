from django.urls import path
from django.shortcuts import render
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('email_verification/', lambda request:render(request, 'account/email/email_verification.html'), name='email_verification'),
]

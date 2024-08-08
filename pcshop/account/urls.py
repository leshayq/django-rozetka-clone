from django.urls import path
from django.shortcuts import render
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('email_verification/', lambda request:render(request, 'account/registration/email_verification.html'), name='email_verification'),
]

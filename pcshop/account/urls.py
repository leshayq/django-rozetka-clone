from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
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

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='account/password/password_reset.html', 
        email_template_name='account/password/password_reset_email.html',
        success_url=reverse_lazy('account:password_reset_done')
        ), 
        name='password_reset'),

    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password/password_reset_done.html'
    ), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password/password_reset_confirm.html',
        success_url=reverse_lazy('account:password_reset_complete')
    ),
        name='password_reset_confirm'),

    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password/password_reset_complete.html'
    ), name='password_reset_complete'),
]

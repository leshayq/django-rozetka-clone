from . import views
from django.urls import path

from .webhooks import stripe_webhook

app_name = 'payment'

urlpatterns = [
    path('shipping/', views.shipping, name='shipping'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-fail/', views.payment_fail, name='payment-fail'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path('stripe_webhook', stripe_webhook, name='webhook-stripe'),
]


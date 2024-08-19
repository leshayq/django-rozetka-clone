from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
import stripe

from cart.cart import Cart
from .forms import ShippingAddressForm
from .models import Order, OrderItem, ShippingAddress
from django.conf import settings 


stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

@login_required(login_url='account:login')
def shipping(request):
    try:
        shipping_adress = ShippingAddress.objects.get(user=request.user)
    except ShippingAddress.DoesNotExist:
        shipping_adress = None

    form = ShippingAddressForm(instance=shipping_adress)

    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=shipping_adress)
        if form.is_valid():
            shipping_adress = form.save(commit=False)
            shipping_adress.user = request.user
            shipping_adress.save()
            form.save()
            return redirect('account:dashboard')
    return render(request, 'payment/shipping.html', {'form': form})

def checkout(request):
    if request.user.is_authenticated:
        shipping_address = ShippingAddress.objects.get_or_create(user=request.user)
        if shipping_address:
            return render(request, 'payment/checkout.html', {'shipping_address': shipping_address})
    return render(request, 'payment/checkout.html')

def complete_order(request):
    if request.method == 'POST':
        full_name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')

        cart = Cart(request)
        total_price = cart.get_total_price()

        shipping_address, _ = ShippingAddress.objects.get_or_create(
            user = request.user,
            defaults={
                'full_name': full_name,
                'email': email,
                'street_address': address,
                'city': city,
                'zip_code': zip_code
            }
        )
        session_data = {
            'mode': 'payment',
            'success_url': request.build_absolute_uri(reverse('payment:payment-success')),
            'cancel_url': request.build_absolute_uri(reverse('payment:payment-fail')),
            'line_items': []
        }

        if request.user.is_authenticated:
            order = Order.objects.create(user=request.user, shipping_address=shipping_address, amount=total_price)

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['qty'], user=request.user)
                
                session_data['line_items'].append({
                    'price_data': {
                        'unit_amount': int(item['price'] * Decimal(100)),
                        'currency': 'usd',
                        'product_data': {
                            'name': item['product']
                        },
                    },
                    'quantity': item['qty'],
                })

                session = stripe.checkout.Session.create(**session_data)
                return redirect(session.url, code=303)
        else:
            order = Order.objects.create(shipping_address=shipping_address, amount=total_price)

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['qty'])

        return JsonResponse({'success': True})

def payment_success(request):
    for key in list(request.session.keys()):
        del request.session[key]
    return render(request, 'payment/payment_success.html')

def payment_fail(request):
    return render(request, 'payment/payment_fail.html')
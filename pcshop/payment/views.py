from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from cart.cart import Cart
from .forms import ShippingAddressForm
from .models import Order, OrderItem, ShippingAddress

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
    return render(request, 'payment/checkout.html')

def complete_order(request):
    return render(request, 'payment/complete_order.html')

def payment_success(request):
    return render(request, 'payment/payment_success.html')

def payment_fail(request):
    return render(request, 'payment/payment_fail.html')
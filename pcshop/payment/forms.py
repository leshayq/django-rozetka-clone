from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'email', 'street_address', 'city', 'zip_code']
        exclude = ('user',)


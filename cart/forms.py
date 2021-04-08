from django import forms
# from django.contrib.auth.models import User
from cart.models import Order

class CheckoutForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Address"}))
    city = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "City"}))
    state = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "State"}))
    zipcode = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Zipcode"}))
    phone = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Phone"}))

    class Meta():
        model = Order
        fields = ['address','city','state','zipcode','phone']
        # fields = '__all__'
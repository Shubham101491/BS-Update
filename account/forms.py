from django import forms
from django.contrib.auth.models import User
# from account.models import Register


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Username"}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Email"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': "Password"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': "Confirm Password"}))

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", 'placeholder': "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", 'placeholder': "Password"}))

    class Meta():
        model = User
        fields = ('username', 'password')

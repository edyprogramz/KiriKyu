from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import PaymentOption

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "your username",
        "class": "input-field"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "your password",
        "class": "input-field"
    }))

class SignupForm(UserCreationForm):
    payment_option = forms.ModelChoiceField(queryset=PaymentOption.objects.all(), empty_label=None)
    account_details = forms.CharField(max_length=255, widget=forms.TextInput(attrs={"placeholder": "Enter account details", "class": "input-field"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'payment_option', 'account_details')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "create a username",
        "class": "input-field"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "enter your email address",
        "class": "input-field"
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "create a password",
        "class": "input-field"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "re-enter the password",
        "class": "input-field"
    }))
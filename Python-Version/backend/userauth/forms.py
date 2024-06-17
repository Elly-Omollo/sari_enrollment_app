from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class signupForm(UserCreationForm):
    fullname = forms.CharField(widget=forms.TextInput(attrs={ 'class':'form-group'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class':'form-group'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class':'form-group'}))
    
    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'phone_number', 'password1', 'password2']
    

    

    

class otpForm(forms.Form):
    otp = forms.CharField(widget=forms.TextInput)
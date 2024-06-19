from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class signupForm(UserCreationForm):
    fullname = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['fullname', 'username', 'email', 'phone_number', 'password1', 'password2']

       
    

    

class otpForm(forms.Form):
    otp = forms.CharField(label="Enter OPT", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        fields = '__all__'
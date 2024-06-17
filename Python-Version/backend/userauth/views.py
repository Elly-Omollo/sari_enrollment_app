from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import  View
from django.contrib import messages
from .forms import otpForm, signupForm

# otp send functions
from .utils import generate_otp, send_otp_mail, send_otp_phone

import datetime
from django.utils import timezone
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login as auth_login
from rest_framework_simplejwt.tokens import RefreshToken
import random

from .models import * 
# from  .forms import loginForm
# Create your views here.


# homepage
def index(request):

    return render(request, "app/index.html")

# login View
class login(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # form = loginForm()
        return render(request, 'login/login.html', {})
    
    def post(self, request, *args, **kwargs):
 
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            print(f"email is-----> \t {email} \tand pass is -----> \t {password}")
            try:
                user_query = User.objects.get(email=email)
                user_auth = authenticate(request, email=email, password=password)
                print(f"Authenticated user: {user_auth}")
                if user_auth is not None:
                   
                    otp = generate_otp()
                    user_query.otp = otp
                    user_query.save()
                    otp_expiry = timezone.now() + datetime.timedelta(minutes=2)
                    max_otp_try = int(user_query.max_otp_try) - 1
                    user_query.otp_expiry = otp_expiry
                    user_query.max_otp_try = max_otp_try
                    user_query.save()

                    # send_otp_phone(user_query.phone_number, otp)
                    # send_otp_mail(email, otp)
                    messages.success(request, f'An otp was sent  to this bumber {user_query.phone_number}')
                    print(f'An otp was sent  to this bumber {user_query.phone_number}')
                    print(f"User found: {user_query}")
                    print(f"User phone number: {user_query.phone_number}")
                    print(f"User OTP: {otp} will expire after 2 minutes from---------> {timezone.now()}")
                    return redirect('otp_page')

                else:
                    messages.error(request, 'Incorrect password')
                    print('your password is incorrect')
                    
            
            except User.DoesNotExist:
                messages.error(request,'User doest not exist')
                # return redirect('userauth:login')
            

            return render(request, 'login/login.html' ) 
    
   
               
# ---------------------end of login view-----------------------


#OTP Verification View
class VerifyOTP(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        form = otpForm()
        return render(request, 'otp/verify_otp.html', {"form":form})

    def post(self, request, *args, **kwargs):
        form = otpForm(request.POST)

        if form.is_valid():
            otp = form.cleaned_data['otp']
            try:
                user = User.objects.get(otp=otp)
                print(user, otp)
                if user.otp_expiry < timezone.now():
                    messages.error(request, "OTP has expired. Please request a new one.")
                    return redirect(request, 'otp/verify_otp.html', {"form": form})
                
                if user:
                    auth_login(request, user)
                    user.otp = None
                    user.otp_expiry = None
                    user.max_otp_try = 3
                    user.otp_max_out = None
                    user.save()
                    refresh = RefreshToken.for_user(user)

                    messages.success(request, f"hey {request.user} Your account has been activated")
                    print(f"hey {request.user} Your account has been activated")
                    messages.success(request, 'Account activate')

                    print('logged in successfully')
                    return redirect('home')
            except User.DoesNotExist:
                messages.error(request, "Invalid OTP.")
                print("Invalid OTP.")
                return redirect('login')
          
        return render(request, 'otp/verify_otp.html', {"form":form})

# --------------------end of Verify otp view -------------------



# creating account view
class signup(View):
    # pass
    def get(self, request):
        form = signupForm()
        return render(request,  "signup/signup.html" , {'form':form})
    
    # post request
    def post(self, request):
        form = signupForm(request.POST)

        if form.is_valid():
            
            fullname = form.cleaned_data.get("fullname") 
            phone = form.cleaned_data.get("phone_number")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
           
            form.save()
            
            print(password, email)
            user = authenticate(email=email, password=password)
            messages.success(request, f"hey {fullname}, \n Your account has been created successfully. with this")
            # print(f"hey {fullname}, your account has been created successfully. with this {email} {password}")
            # auth_login(request, user)
            return redirect('login')
        return render(request, 'signup/signup.html', {'form':form})



# logout page
def logout(request):
    return HttpResponse("<h1 style='text-align:center;color:blue;'>You have just loged out. You can login again</h1>")


from django.urls import path
from . import views
from .views import signup, login, VerifyOTP


urlpatterns = [
    path("login/", login.as_view(), name="login"),
    path("signup/", signup.as_view() , name="signup"),
    path("verify-otp/", VerifyOTP.as_view() , name="otp_page"),
    path("logout/", views.logout , name="logout")
]
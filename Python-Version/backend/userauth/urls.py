from django.urls import path
from . import views


urlpatterns = [

    path("", views.index , name="home-page"),
    path("login/", views.login , name="login"),
    path("signup/", views.signup , name="create-account"),
    path("logout/", views.logout , name="logout")
]
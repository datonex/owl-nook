from django.urls import path
from django.conf.urls import url
from .views import UserLoginView, UserRegisterView, logout_view

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
]

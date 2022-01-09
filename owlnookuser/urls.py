from django.urls import path
from django.conf.urls import url
from .views import UserRegisterView

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
]

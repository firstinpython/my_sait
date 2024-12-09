from django.urls import path
from .views import sign_in,sign_up,profile

urlpatterns = [
    path("sign_in",sign_in),
    path("sign_up",sign_up),
    path("profile",profile)
]
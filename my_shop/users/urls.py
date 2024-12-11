from django.urls import path
from .views import LoginUser, UserRegistrationView, UserProfileView

app_name = "users"
urlpatterns = [
    path("sign_in",LoginUser.as_view(),name="sing-in"),
    path("sign_up",UserRegistrationView.as_view()),
    path("profile",UserProfileView.as_view())
]
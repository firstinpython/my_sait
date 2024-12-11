from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import Users


class SignIn_User(AuthenticationForm):

    class Meta:
        model = Users
        fields = ("username", "password")


class SignUp_User(UserCreationForm):
    class Meta:
        model = Users
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class Profile(UserChangeForm):
    class Meta:
        model = Users
        fields = ("username", "first_name", "last_name",  "email")

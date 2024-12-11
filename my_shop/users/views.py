from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required


from .forms import SignIn_User, SignUp_User,Profile
from .models import Users
# Create your views here.


class LoginUser(LoginView):
    form_class = SignIn_User
    template_name = 'users/sign_in.html'

    def get_success_url(self):
        return reverse_lazy('product:product')

class UserRegistrationView(CreateView):
    model = Users
    template_name = 'users/sign_up.html'
    form_class = SignUp_User
    success_url = reverse_lazy('product:product')

class UserProfileView(UserPassesTestMixin,UpdateView):
    model = Users
    form_class =  SignUp_User
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile',args=(self.object.id,))

    def test_func(self):
        return self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect('users:sign_in')


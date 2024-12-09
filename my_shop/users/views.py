from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import SignIn_User, SignUp_User,Profile
from .models import Users
# Create your views here.

def sign_in(request):
    if request.method == "POST":
        form = SignIn_User(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request,user)
                return HttpResponse("ok")
        return HttpResponse("no ok")
    form = SignIn_User()
    return render(request,"users/sign_in2.html",context={"form":form})


def sign_up(request):
    if request.method == "POST":
        form = SignUp_User(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("ok")
    form = SignUp_User()
    return render(request,"users/sign_up.html",context={"form":form})

@login_required()
def profile(request):
    if request.method == "POST":
        form = Profile(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("ok")
        else:
            return HttpResponse(form.errors)
    form = Profile()
    return render(request,"users/profile.html",context={"form":form})

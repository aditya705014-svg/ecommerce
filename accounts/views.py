from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("store") 
        else:
              return render(request, "accounts/login.html")

    return render(request, "accounts/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken please try another ")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)#ye ek built in fuction hai jisee username 
        #aur password ko store karta hai data base me jisse login rejister hota hai
        messages.success(request, "Account created successfully! Please login.")
        return redirect("login")

    return render(request, "accounts/register.html")

@login_required(login_url="login")
def index(request):
    return render(request, "accounts/index.html")


def user_logout(request):
    logout(request)
    return redirect("login")


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from accounts.forms import RegistrationForm


# Create your views here.
def index(requet):
    if requet.user.is_authenticated:
        return render(requet, "accounts/yay.html")
    return HttpResponse(
        "Hello, world. You're at the accounts index. <a href='/accounts/login_user'>Login</a>"
    )


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            form.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("index")
    else:
        form = RegistrationForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.success(request, "Error Logging in, Please try again")
            return redirect("login")
    else:
        return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect("index")

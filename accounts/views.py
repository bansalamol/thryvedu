from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def index(request):
    return render(request, "frontend/index.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect("login")
        else:
            messages.error(request, "There was an error during registration.")
    else:
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful! Welcome back.")
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "auth/login.html", {"form": form})


def about_us(request):
    context = {
        "company_name": "Edu Portal",
        "description": "Edu Portal is an innovative platform for online learning.",
        "team_members": ["Alice", "Bob", "Charlie", "David"],
    }
    return render(request, "frontend/about.html", context)


@login_required(login_url="login")
def dashboard_view(request):
    return render(request, "backend/dashboard.html")


def user_logout(request):
    logout(request)

    return redirect("login")

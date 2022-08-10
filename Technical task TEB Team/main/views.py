from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from datetime import date
from . import services
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


@login_required(login_url='login')
def IndexView(request):
    """Index page view"""
    date_today = date.today().strftime("%Y-%m-%d")
    username = request.user.username

    if request.method == "POST":
        date_from, date_to = request.POST.get('from'), request.POST.get('to')
    else:
        date_from = date_to = date_today

    context = {
            "date_today": date_today,
            "date_from": date_from,
            "date_to": date_to,
            "username": username,
            "clicks": services.get_clicks_count(username, date_from, date_to),
            "conversions": services.get_conversions_count(username, date_from, date_to)
        }

    return render(request, 'main/index.html', context=context)


def LoginView(request):
    """Login page view"""
    if request.user.is_authenticated:
        return redirect('index')

    form = forms.LoginForm()

    if request.method == "POST":
        username, password = request.POST.get('username'), request.POST.get('password')

        try:
            models.CustomUser.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "There is no User with this username")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Password is incorrect")
            return redirect('login')

    context = {
        'form': form,
        }

    return render(request, 'main/login.html', context=context)


def LogoutView(request):
    """Logout page view"""
    logout(request)
    return redirect('index')

from django.http import HttpResponse
from django.shortcuts import render
from . import models
from django.contrib.auth.models import User


def IndexView(request):
    user = User.objects.get(username="admin")
    print(user.user_permissions)
    return HttpResponse("It works!")

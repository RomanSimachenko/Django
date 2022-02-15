import email
import imp
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from .. import forms
from ...base import services


def _get_form():
    """Returns the standard(clear) user creation form"""
    return forms.CustomUserCreationForm()


def request_post(request):
    """Processing form, validates data from request"""
    try:
        User.objects.get(username=request.POST.get(
            'username').lower(), email=request.POST.get("email"))
        messages.error(
            request, "User with that username and email already registered! Try to login!")
        return redirect('register')
    except:
        pass

    try:
        User.objects.get(username=request.POST.get('username').lower())
        messages.error(request, "User with that username already registered!")
        return redirect('register')
    except:
        pass

    try:
        User.objects.get(email=request.POST.get('email'))
        messages.error(request, "User with that email already registered!")
        return redirect('register')
    except:
        pass

    form = forms.CustomUserCreationForm(request.POST)

    if form.is_valid():
        return _form_valid(form)
    else:
        messages.error(request, "Form is invalid!")
        return redirect('register')


def _form_valid(form):
    """Additionally validates form and creates new user"""
    new_user = form.save(commit=False)
    new_user.username = new_user.username.lower()
    new_user.is_active = False

    new_user.save()

    username = services.encode_and_decode_message(new_user.username, 'encode')
    token = services.generate_token()
    token = services.encode_and_decode_message(token, "encode")

    return redirect("verify-email", data1=username, data2=token)

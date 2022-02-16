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

    services.send_message_to_email(new_user.email, "http://localhost:8000/check-verify/" +
                                   services.encode_and_decode_message(new_user.username, "encode") + "/")

    return redirect("message")

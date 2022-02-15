from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings
from ...base import services


def request_post(request):
    """Gets username/email and password from request and processing it"""
    username_or_email = request.POST.get("username_email")
    username_or_email = username_or_email if "@" in username_or_email else username_or_email.lower()
    password = request.POST.get("password")

    try:
        user = User.objects.get(username=username_or_email)
        return _authenticate_user(request, username_or_email, password)
    except:
        try:
            user = User.objects.get(email=username_or_email)
            return _authenticate_user(request, username_or_email, password)
        except:
            messages.error(request, "User doesn't exists!")
            return redirect('login')


def _authenticate_user(request, username_email, password):
    """Authenticates and logins user"""
    if "@" in username_email:
        base_user = User.objects.get(email=username_email)
        if not base_user.is_active:
            username = base_user.username
            token = services.generate_token()
            return redirect("verify-email", data1=services.encode_and_decode_message(username, "encode"),
                            data2=services.encode_and_decode_message(token, "encode"))
        else:
            user = authenticate(
                request, username=base_user.username, password=password)
    else:
        base_user = User.objects.get(username=username_email)
        if not base_user.is_active:
            username = base_user.username
            token = services.generate_token()
            return redirect("verify-email", data1=services.encode_and_decode_message(username, "encode"),
                            data2=services.encode_and_decode_message(token, "encode"))
        else:
            user = authenticate(
                request, username=username_email, password=password)

    if user is not None:
        login(request, user)
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        messages.error(request, "Password isn't right!")
        return redirect('login')

from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .services import register, login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from ..base import services
from django.contrib.auth.models import User


def index(request):
    """Main page of the site"""
    return render(request, "main/index.html", {})


def RegisterView(request):
    """Register user page"""
    if request.user.is_authenticated:
        return redirect('index')

    form = register._get_form()

    if request.method == 'POST':
        return register.request_post(request)

    return render(request, "main/register.html", {'form': form})


def LoginView(request):
    """Login user page"""
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        return login.request_post(request)

    return render(request, "main/login.html", {})


def LogoutView(request):
    """Logout user view"""
    logout(request)

    return redirect(settings.LOGOUT_REDIRECT_URL)


@login_required(login_url=settings.LOGIN_URL)
def UserProfileView(request, id):
    """User profile page with all information"""
    user = services.get_user_object_by_id(id)

    return render(request, "main/user-profile.html", {'user': user})


def MessageView(request):
    """Message to user page"""
    if request.user.is_authenticated:
        return redirect('index')

    return render(request, "main/message.html", {"message_text": "Verification link was sent to your email."})


def CheckVerifyView(request, data1):
    """Check code and user email"""
    if request.user.is_authenticated:
        return redirect('index')

    if len(data1) % settings.TOKEN_REPEATS != 0:
        return redirect("index")

    if data1.count(data1[:len(data1) // settings.TOKEN_REPEATS]) != settings.TOKEN_REPEATS:
        return redirect("index")

    username = services.encode_and_decode_message(data1, "decode")
    try:
        base_user = User.objects.get(username=username)
    except:
        return redirect("index")
    base_user.is_active = True
    base_user.save()

    return render(request, "main/message.html", {"message_text": "Your email verified!"})

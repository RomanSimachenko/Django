from django.shortcuts import redirect, render
from django.contrib.auth import logout
from .services import register, login
from django.conf import settings
from django.contrib.auth.decorators import login_required
from ..base import services
from django.contrib.auth.models import User
from .services import verify_email


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


def VerifyEmailView(request, data1, data2):
    """Verify email page, sends code to user email and checks it"""
    if request.user.is_authenticated:
        return redirect('index')

    if data1[:len(data1) // 2] != data1[len(data1) // 2:] or data2[:len(data2) // 2] != data2[len(data2) // 2:]:
        return redirect("index")

    username = services.encode_and_decode_message(data1, "decode")
    user = User.objects.get(username=username)
    token = services.encode_and_decode_message(data2, "decode")

    try:
        if len(token) != settings.TOKEN_LENGTH:
            return redirect('index')
        for symbol in token:
            if symbol not in settings.TOKEN_SYMBOLS:
                return redirect('index')
    except:
        return redirect('index')

    try:
        User.objects.get(username=username)
    except:
        return redirect('index')

    if request.method == "POST":
        return verify_email.check_entered_code(request, user, data1, token)
    else:
        verify_email.send_code(user.email, token)

    return render(request, "main/verify-email.html", {"user": user})

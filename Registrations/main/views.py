from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from . import forms
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import int_to_base36, base36_to_int
import base64


def encode_and_decode(message, do):
    """Encodes and decodes given message"""
    if do.strip().lower() == 'encode':
        message = message
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        return base64_message
    else:
        base64_message = message
        base64_bytes = base64_message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded = message_bytes.decode('ascii')
        return decoded


def IndexView(request):
    """Main page"""
    return render(request, "main/index.html", {})


def RegisterView(request):
    """Register user page"""
    if request.user.is_authenticated:
        return redirect("index")

    form = forms.CustomUserCreationForm()

    if request.method == 'POST':
        try:
            User.objects.get(username=request.POST.get("username"))
            messages.error(
                request, "User with that username already exists!")
            return redirect("register")
        except:
            pass
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            subject = "Django verification email"
            uid = encode_and_decode(str(user.id), 'encode')
            email = encode_and_decode(user.email, 'encode')
            body = f"""http://127.0.0.1:8000/verify_email/{uid}/{email}/"""

            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return redirect("verify_email_complete")
        else:
            messages.error(request, "Form is invalid!")
            return redirect("register")

    return render(request, "main/register.html", {"form": form})


def VerifyEmailCompleteView(request):
    """Verify email complete page"""
    return render(request, "main/email_verify_complete.html")


def VerifyEmailView(request, uid, email):
    """Verification email page"""
    uid = int(encode_and_decode(uid, 'decode'))
    email = encode_and_decode(email, 'decode')
    try:
        user = User.objects.get(id=uid, email=email)
    except:
        return redirect("verify_email_complete")
    user.is_active = True
    user.save()
    return redirect("verify_email_done")


def VerifyEmailDoneView(request):
    """Verify email done page"""
    return render(request, "main/email_verify_done.html")


def ProfileView(request, pk):
    """User profile page"""
    user = User.objects.get(id=pk)

    return render(request, "main/user-profile.html", {'user': user})

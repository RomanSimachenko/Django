from django.core.mail import send_mail
from django.conf import settings
from ...base import services
from django.contrib import messages
from django.shortcuts import redirect


def check_entered_code(request, user, data1, token):
    """Checks if entered code == email token"""
    entered_code = request.POST.get('code')
    if entered_code.strip() == token:
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        messages.error(request, "Неверный код! Отправили новый.")
        new_token = services.generate_token()
        return redirect("verify-email", data1, services.encode_and_decode_message(new_token, "encode"))


def send_code(email, token):
    """Sends token to the user email"""
    send_mail(
        'Django',
        f'Your verification token: {token}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

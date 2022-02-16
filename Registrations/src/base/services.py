from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
import base64


def get_user_object_by_id(pk):
    """Returns user-object got by id"""
    return User.objects.get(id=pk)


def encode_and_decode_message(message, do):
    """Encodes and decodes message using base64"""
    if do.lower() == 'encode':
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        return base64_bytes.decode('ascii') * settings.TOKEN_REPEATS
    else:
        message_bytes = message[:len(
            message) // settings.TOKEN_REPEATS].encode('ascii')
        base64_bytes = base64.b64decode(message_bytes)
        return base64_bytes.decode('ascii')


def send_message_to_email(email, link):
    """Sends message to the user email"""
    send_mail(
        'Django',
        f'Your verification link: {link}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )

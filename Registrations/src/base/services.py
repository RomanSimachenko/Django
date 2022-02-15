from django.contrib.auth.models import User
from django.conf import settings
import random
import base64


def get_user_object_by_id(pk):
    """Returns user-object got by id"""
    return User.objects.get(id=pk)


def encode_and_decode_message(message, do):
    """Encodes and decodes message using base64"""
    if do.lower() == 'encode':
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        return base64_bytes.decode('ascii') * 2
    else:
        message_bytes = message[:len(message) // 2].encode('ascii')
        base64_bytes = base64.b64decode(message_bytes)
        return base64_bytes.decode('ascii')


def generate_token():
    """Generates token for verify"""
    all_possible = list(settings.TOKEN_SYMBOLS)
    token = ""
    for _ in range(settings.TOKEN_LENGTH):
        choice_symbol = random.choice(all_possible)
        token += choice_symbol
        del all_possible[all_possible.index(choice_symbol)]

    return token

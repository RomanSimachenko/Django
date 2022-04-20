from . import services
from django.shortcuts import redirect, render
from django.http import HttpResponse
from string import punctuation

punctuation_symbols = set(punctuation)


def ItemView(request):
    """Item text page"""
    pk = request.GET.get('id', None)

    try:
        int(pk)
    except:
        return HttpResponse("ID is't valid!")

    body = services.get_text(id=pk)

    splitted = body.split()
    text = ""
    for word in splitted:
        text += word
        if len(word) == 6:
            text += "™"
        text += " "

    return HttpResponse(text)

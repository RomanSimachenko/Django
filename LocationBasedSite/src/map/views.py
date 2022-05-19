from django.shortcuts import render


def IndexView(request):
    return render(request, 'map/index.html', context={})
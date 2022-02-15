from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('index')

    return render(request, 'google_auth/index.html', {})

from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import JsonResponse
from . import serializers
from . import models
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def loginUser(request):
    """Login page"""
    if request.user.is_authenticated:
        return redirect('home')

    form = forms.UserLoginForm()

    if request.POST:
        form = forms.UserLoginForm(request.POST)
        username = form['username'].value()
        password = form['password'].value()

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist")
            return redirect('login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password doesn't exist")
            return redirect('login')

    return render(request, 'company/login.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('home')


def index(request):
    """Index(main) page"""
    employees = models.Employee.objects.order_by('-join_date')[:50]

    return render(request, 'company/index.html', {'employees': employees})


@login_required(login_url='login')
def EmployeeList(request):
    """List of employees page"""
    if request.POST:
        search = request.POST.get('search', default='')
        employees = models.Employee.objects.filter(
            Q(fio__icontains=search) |
            Q(position__icontains=search) |
            Q(chief__name__icontains=search) |
            Q(join_date__icontains=search)
        )
    else:
        employees = models.Employee.objects.all()

    return render(request, 'company/employee_list.html', {'employees': employees})


@login_required(login_url='login')
def EmployeesAjax(request):
    ordering = request.GET.get('ordering', default='')
    search = request.GET.get('search', default='')
    ordering = '-join_date' if ordering == 'join_date' else ordering
    if ordering and search:
        employees = models.Employee.objects.filter(
            Q(fio__icontains=search) |
            Q(position__icontains=search) |
            Q(chief__name__icontains=search) |
            Q(join_date__icontains=search)
        ).order_by(ordering)
    elif ordering:
        employees = models.Employee.objects.order_by(ordering)
    elif search:
        employees = models.Employee.objects.filter(
            Q(fio__icontains=search) |
            Q(position__icontains=search) |
            Q(chief__name__icontains=search) |
            Q(join_date__icontains=search)
        )
    else:
        employees = models.Employee.objects.all()
    serializer = serializers.EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)

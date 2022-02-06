from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.index, name='home'),

    path('employees/', views.EmployeeList, name='employees'),
    path('employees-ajax/', views.EmployeesAjax, name='employees-ajax')
]

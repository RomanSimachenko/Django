from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'date_joined',)

from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    """Products"""
    list_display = ("title", "price", 'add_date',)

from tabnanny import verbose
from turtle import title
from django.apps import AppConfig


class ShopsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shops_app'
    verbose_name = "shops app"

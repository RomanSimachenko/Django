from django.db import models
from src.base import services


class Chief(models.Model):
    name = models.CharField("Chief's name", max_length=150)


class Employee(models.Model):
    fio = models.CharField("ФИО", max_length=150, validators=[
                           services.validate_fio])
    avatar = models.ImageField("Аватар", upload_to="company/")
    position = models.CharField("Должность", max_length=100)
    chief = models.ForeignKey(Chief, on_delete=models.CASCADE)
    join_date = models.DateField(
        "Дата приёма на роботу", help_text="format: YYYY-MM-DD")
    salary = models.PositiveIntegerField("Заработная плата")

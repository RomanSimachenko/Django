from django import forms
from . import models


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.CustomUser
        fields = ("username", "password")

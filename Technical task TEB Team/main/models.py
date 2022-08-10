from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomUser(AbstractUser):
    """Custom User model"""
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now, null=True, blank=True)
    first_name = models.CharField(_("first name"), max_length=150, null=True, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, null=True, blank=True)
    email = models.EmailField(_("email address"), null=True, blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ()


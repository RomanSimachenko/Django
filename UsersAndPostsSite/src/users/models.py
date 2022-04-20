from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    about = models.CharField(_("About"), max_length=500)
    avatar = models.ImageField(
        "Avatar", blank=True, default="avatars/default.jpg", upload_to="avatars/")

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ("email",)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ('-date_joined',)
        verbose_name = _("user")
        verbose_name_plural = _("users")

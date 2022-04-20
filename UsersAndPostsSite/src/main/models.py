from django.db import models
from django.utils.translation import gettext as _
from src.users.models import CustomUser


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_(
        "User's comment"))
    title = models.CharField(_("Title"), max_length=300)
    body = models.CharField(_("Body"), max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name="user", verbose_name=_("user's post"))
    title = models.CharField(_("Title"), max_length=300)
    image = models.ImageField(_("Image"), blank=True,
                              null=True, upload_to="posts/")
    short_description = models.CharField(
        _("Short description"), max_length=1000, blank=True, null=True)
    description = models.TextField(_("Description"))
    liked = models.ManyToManyField(
        CustomUser, related_name="users", verbose_name="User's likes")
    comments = models.ManyToManyField(
        Comment, related_name="comments", verbose_name=_("Post's comments"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title


class Follower(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name=_("User"))
    followers = models.ManyToManyField(
        CustomUser, related_name="folowers", verbose_name=_("User's folowers"))

    class Meta:
        verbose_name = _("Follower")
        verbose_name_plural = _("Followers")

    def __str__(self):
        return self.user.username

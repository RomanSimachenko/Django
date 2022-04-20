from dataclasses import fields
from django import forms
from . import models


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'image', 'short_description', 'description',)


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('title', 'body',)

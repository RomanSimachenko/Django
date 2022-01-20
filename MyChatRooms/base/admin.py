from django.contrib import admin
from .models import Topic, Room, Message, User

admin.site.register(User)

admin.site.register(Topic)

admin.site.register(Room)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'room', 'body',)

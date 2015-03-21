from django.contrib import admin
from persistent_messages.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['level', 'user', 'from_user', 'subject', 'message', 'created', 'read', 'is_persistent']


admin.site.register(Message, MessageAdmin)

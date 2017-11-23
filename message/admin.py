from django.contrib import admin

from message.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ['parent_username', 'status', 'recipient_email', 'title_text']
    ordering = ['-created']

    class Meta:
        model = Message


admin.site.register(Message, MessageAdmin)

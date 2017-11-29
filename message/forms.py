from django import forms

from .models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title_text', 'text', 'recipient_email']

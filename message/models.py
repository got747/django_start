from __future__ import unicode_literals

from django.core.mail import EmailMessage
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):

    SENT = 1
    NOT_SENT = 2

    AVAILABLE_CHOICES = (
        (SENT, 'Отправлено'),
        (NOT_SENT, 'Не отправлено')
    )

    recipient_email = models.EmailField(default='')
    text = models.TextField(blank=True)
    title_text = models.CharField(max_length=100, blank=True)
    parent_username = models.ForeignKey('auth.User')

    created = models.DateTimeField(default=timezone.now)
    status = models.SmallIntegerField(verbose_name='статус отправки сообщения', choices=AVAILABLE_CHOICES)


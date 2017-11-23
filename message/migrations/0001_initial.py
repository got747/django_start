# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-15 22:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_email', models.EmailField(default='', max_length=254)),
                ('text', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.SmallIntegerField(choices=[(1, 'Отправлено'), (2, 'Не отправлено')])),
                ('parent_username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

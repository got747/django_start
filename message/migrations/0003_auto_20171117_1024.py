# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20171116_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='title_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

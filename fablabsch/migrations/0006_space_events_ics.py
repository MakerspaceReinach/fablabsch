# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-05 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fablabsch', '0005_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='events_ics',
            field=models.URLField(blank=True, max_length=800, verbose_name='events_ics'),
        ),
    ]

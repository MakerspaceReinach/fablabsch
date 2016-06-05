# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-05 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fablabsch', '0004_disable_unique_social_on_space'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('uid', models.CharField(max_length=200,  primary_key=True, serialize=False, verbose_name='uid')),
                ('startdate', models.DateTimeField(verbose_name='startdate')),
                ('enddate', models.DateTimeField(verbose_name='enddate')),
                ('modified', models.DateTimeField(verbose_name='modified')),
                ('summary', models.TextField(blank=True, verbose_name='summary')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('location', models.CharField(blank=True, max_length=200, verbose_name='location')),
                ('image_src', models.URLField(blank=True, max_length=800, verbose_name='external image url')),
                ('image', models.ImageField(blank=True, null=True, upload_to='event', verbose_name='image')),
                ('space', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='fablabsch.Space', verbose_name='space')),
            ],
            options={
                'ordering': ('-startdate',),
            },
        ),
    ]

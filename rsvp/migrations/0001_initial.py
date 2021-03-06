# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-27 00:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('guests', models.IntegerField()),
                ('comments', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]

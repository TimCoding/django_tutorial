# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='type',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]

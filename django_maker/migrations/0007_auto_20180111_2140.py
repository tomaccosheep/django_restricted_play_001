# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-11 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_maker', '0006_auto_20180111_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play_project',
            name='unique_id',
            field=models.CharField(default='qq2OjRX4HBp8Bzd6svajxEEF0nHM8RCK', max_length=32, primary_key=True, serialize=False),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-12 00:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_maker', '0013_auto_20180112_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play_project',
            name='unique_id',
            field=models.CharField(default='5BIoOirzIUukU4gco4C4h1TsuGmwy0Wr', max_length=32, primary_key=True, serialize=False),
        ),
    ]

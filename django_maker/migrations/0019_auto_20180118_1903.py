# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-18 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_maker', '0018_auto_20180118_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play_project',
            name='unique_id',
            field=models.CharField(default='6ZWwBBtyB2YzC8vgDNfZdZ4YQhjm34NL', max_length=32, primary_key=True, serialize=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-18 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_maker', '0014_auto_20180112_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play_project',
            name='unique_id',
            field=models.CharField(default='8VH4JYvRI7WAlse45mdluYNOzfXTz2Sc', max_length=32, primary_key=True, serialize=False),
        ),
    ]

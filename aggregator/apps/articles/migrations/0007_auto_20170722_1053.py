# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20170722_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='public_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]

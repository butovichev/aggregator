# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20170722_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
    ]

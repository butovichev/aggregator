# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_public_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

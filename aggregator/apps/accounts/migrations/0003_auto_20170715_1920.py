# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 19:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170713_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partnerprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='partner_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('domain_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(editable=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
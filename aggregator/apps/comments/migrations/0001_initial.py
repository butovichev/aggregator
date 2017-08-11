# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_auto_20170716_1707'),
        ('quests', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('text', models.TextField()),
                ('gamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Gamer')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quests.Quest')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.Rating'),
        ),
    ]

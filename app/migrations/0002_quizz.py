# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-08-23 00:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quizz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('subtitle', models.CharField(max_length=1000)),
                ('url', models.CharField(max_length=1000)),
            ],
        ),
    ]
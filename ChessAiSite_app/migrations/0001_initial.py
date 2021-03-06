# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-02-08 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(default='', max_length=50)),
                ('isActive', models.BooleanField(default='')),
                ('activationcode', models.CharField(default='', max_length=101)),
                ('playersturn', models.CharField(max_length=2)),
                ('gamebourd', models.CharField(max_length=10000)),
            ],
        ),
    ]

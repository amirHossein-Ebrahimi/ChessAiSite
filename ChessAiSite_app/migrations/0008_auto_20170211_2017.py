# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-02-11 20:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChessAiSite_app', '0007_auto_20170210_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='gamebourd',
            new_name='gameboard',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 11, 20, 17, 32, 93911), max_length='50'),
        ),
    ]

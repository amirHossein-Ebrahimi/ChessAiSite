from __future__ import unicode_literals
from django.db import models,IntegrityError
from datetime import datetime,timedelta

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, default='')
    isActive = models.IntegerField(default=0)
    activationcode = models.CharField(max_length=20, default='')
    gameboard = models.CharField(max_length=100)
    first_time = models.DateTimeField(max_length="50", default=datetime.now())


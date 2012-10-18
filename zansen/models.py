from django.db import models
from datetime import datetime

class User(models.Model):
    name = models.CharField(max_length=256)
    hash = models.CharField(max_length=256)

class Message(models.Model):
    sender = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)

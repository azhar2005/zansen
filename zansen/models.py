from django.db import models

class User(models.Model):
    name = models.CharField(max_length=256)
    hash = models.CharField(max_length=256)

class Message(models.Model):
    message = models.TextField()
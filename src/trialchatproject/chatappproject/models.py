from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    # objects = models.Manager()
    name = models.CharField(max_length=1000, default="")

class Message(models.Model):
    # objects = models.Manager()
    value = models.CharField(max_length=10000, default="")
    date = models.DateTimeField(default=datetime.now , blank= True)
    user = models.CharField(max_length=10000, default="")
    room = models.CharField(max_length=10000, default="")
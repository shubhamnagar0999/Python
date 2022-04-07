
from django.db import models

# Create your models here.
class Chat(models.Model):
    chat = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now=True)
    g = models.ForeignKey("Group", on_delete=models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length=30)
    
from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
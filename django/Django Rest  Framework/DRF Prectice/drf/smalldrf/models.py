from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.IntegerField()
    
    
    
class Forclassview(models.Model):
    na = models.CharField(max_length=50)
    lna = models.CharField(max_length=50)


from django.db import models

# Create your models here.

class Teacher(models.Model):
    tname = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    def __str__(self) :
        return self.tname



class Student(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='studends')
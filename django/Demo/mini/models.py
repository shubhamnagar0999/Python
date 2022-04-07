from operator import mod
from django.db import models

# Create your models here.
class Detail(models.Model):
    Name = models.CharField(max_length=20)
    Last = models.CharField(max_length=20)
    Email = models.EmailField(max_length=20)
    Phone_no = models.IntegerField()

    # def __str__(self):
    #     return self.Name
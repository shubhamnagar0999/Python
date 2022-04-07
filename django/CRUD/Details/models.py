
from django.db import models

# Create your models here.
class Detail(models.Model):
    Name = models.CharField(max_length=50)
    LName = models.CharField(max_length=50)
    Phone = models.IntegerField(50)
    Email = models.EmailField(max_length=50)
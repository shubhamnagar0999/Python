
from django.db import models

# Create your models here.
class signup(models.Model):
    user = models.CharField(max_length=20)
    email = models.EmailField()
    name = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
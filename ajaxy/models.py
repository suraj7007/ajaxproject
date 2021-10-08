from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=70, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50, unique=True)
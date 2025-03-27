from symtable import Class

from django.contrib.auth.password_validation import password_changed
from django.db import models
# Create your models here.

class Menu4(models.Model):
    name=models.CharField(max_length=30,unique= True)
    price=models.FilePathField(max_length=20)
    img = models.ImageField(max_length=10)
    is_buy=models.BooleanField(default=False)
class User(models.Model):
    name=models.CharField(max_length=20,unique= True)
    password=models.CharField(max_length=40)
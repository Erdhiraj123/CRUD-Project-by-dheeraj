from django.db import models


# Create your models here.
class User(models.Model):

    studentname=models.CharField(max_length=100)
    teachername=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

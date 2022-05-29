from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Contact(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    zip = models.IntegerField()


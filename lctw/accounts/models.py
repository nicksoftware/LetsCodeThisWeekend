from django.db import models

# Create your models here.

class UserMoreDetail(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE,default="")
    position = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    zip_code  = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    telephone = models.CharField(max_length=14)


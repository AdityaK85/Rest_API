from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    created_dt = models.DateTimeField(null=True,blank=True)


class login(models.Model):
    mobile = models.CharField(max_length=100)
    profile_image = models.FileField(upload_to='profile_image')
    verify_otp = models.CharField(max_length=100, null=True)
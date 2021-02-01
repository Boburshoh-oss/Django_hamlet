from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.

class Region(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class District(models.Model):
    name=models.CharField(max_length=30)
    region_id=models.ForeignKey(Region, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Type(models.Model):
    name=models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Status(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class View(models.Model):
    name = models.CharField(max_length=20, default=1)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    location=models.CharField(max_length=30)
    Agents=models.CharField(max_length=25,default='Boburbek')
    Beds=models.IntegerField(default=1)
    Bathroom=models.IntegerField(default=1)
    type = models.ForeignKey(View, on_delete=models.CASCADE, null=True)
    Price=models.FloatField()
    imagae=models.ImageField(upload_to='pictures')
    foydalanuvchi=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    region=models.ForeignKey(Region,on_delete=models.CASCADE, null=True, blank=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE, null=True,blank=True)
    status=models.ForeignKey(Status, on_delete=models.CASCADE, null=True,blank=True)
    phone=models.CharField(max_length=30, null=True)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return self.location
     
     
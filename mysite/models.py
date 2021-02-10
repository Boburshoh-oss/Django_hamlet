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



class Status(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class View(models.Model):
    name = models.CharField(max_length=20, default=1)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    title=models.CharField(max_length=40,null=True)
    location=models.CharField(max_length=30)
    Agents=models.CharField(max_length=25)
    Beds=models.IntegerField(default=1)
    Bathroom=models.IntegerField(default=1)
    Property_type = models.ForeignKey(View, on_delete=models.CASCADE, null=True)
    Price=models.FloatField()
    image=models.ImageField(upload_to='pictures')
    author=models.CharField(max_length=40)
    region=models.ForeignKey(Region,on_delete=models.CASCADE, null=True, blank=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE, null=True,blank=True)
    status=models.ForeignKey(Status, on_delete=models.CASCADE, null=True,blank=True)
    phone=models.CharField(max_length=30, null=True)
    date=models.DateField(auto_now=True)
    modum = models.TextField()
    
    def __str__(self):
        return self.location
     
     
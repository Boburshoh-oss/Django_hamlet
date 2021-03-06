from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date



# Create your models here.

class Region(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class District(models.Model):
    name=models.CharField(max_length=50)
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

class AgentModel(models.Model):
    name=models.CharField(max_length=30)
    image=models.ImageField(upload_to="Agents")
    location=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    phone=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Announcement(models.Model):
    
    SEMESTER_CHOICES = (
        ("5000", "5000"),
        ("10000", "10000"),
        ("50000", "50000"),
        ("100000", "100000"),
        ("200000", "200000"),
        ("300000", "300000"),
        ("400000", "400000"),
        ("500000", "500000"),
        ("600000", "600000"),
        ("700000", "500000"),
        ("800000", "800000"),
        ("900000", "900000"),
        ("1000000", "1000000"),
        ("2000000", "2000000"),
    )
    title=models.CharField(max_length=40,null=True)
    location=models.CharField(max_length=30)
    Agents=models.ForeignKey(AgentModel, on_delete=models.CASCADE, null=True)
    Beds=models.IntegerField(default=1)
    Bathroom=models.IntegerField(default=1)
    Property_type = models.ForeignKey(View, on_delete=models.CASCADE, null=True)
    Price=models.PositiveIntegerField("Price")
    image=models.ImageField(upload_to="pictures")
    author=models.CharField(max_length=40)
    person_name=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    region=models.ForeignKey(Region,on_delete=models.CASCADE, null=True, blank=True)
    district=models.ForeignKey(District,on_delete=models.CASCADE, null=True,blank=True)
    status=models.ForeignKey(Status, on_delete=models.CASCADE, null=True,blank=True)
    phone=models.CharField(max_length=30, null=True)
    date=models.DateField(auto_now=True,null=True)
    time_start = models.TimeField(auto_now=True,null=True)
    modum = models.TextField()
    Garage=models.IntegerField(default=0, null=True,blank=True)
    
    def __str__(self):
        return self.location




class Message(models.Model):
    name=models.CharField(null=True,max_length=50)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self):
        return self.name
    

   
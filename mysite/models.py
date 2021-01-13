from django.db import models

# Create your models here.
class Announcement(models.Model):
     location=models.CharField(max_length=30, default='City/Locality Name')
     Property_Type=models.CharField(max_length=60,default='Type')
     Agents=models.CharField(max_length=25,default='Boburbek')
     Beds=models.IntegerField(default=1)
     Bathroom=models.IntegerField(default=1)
     Price=models.FloatField()
     imagae=models.ImageField(upload_to='pictures')
     def __str__(self):
         return self.location
     
     
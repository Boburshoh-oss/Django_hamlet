from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# class Subscribe(models.Model):
#     email_id = models.EmailField(null = True, blank = True)
#     timestamp = models.DateTimeField(default=timezone.now)
#     def __str__(self):
#         return self.email_id
class UserDetail(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    author_image= models.ImageField(default='author_image/author.jpg', upload_to='author_image', null=True, blank=True)
    phone       = models.CharField(max_length=20, default="+998", null=True, blank=True)
    

    class Meta:
        verbose_name = ("UserDetail")
        verbose_name_plural = ("UserDetails")

    def __str__(self):
        return self.user.username


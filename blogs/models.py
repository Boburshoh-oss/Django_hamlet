from django.db import models
from taggit.managers import TaggableManager
from mysite.models import AgentModel
from django.contrib.auth.models import User
# Create your models here.

class Post_categorie(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title           = models.CharField(max_length=250)
    post_image      = models.ImageField(upload_to='blog_rasm')
    categories      = models.ForeignKey(Post_categorie, on_delete=models.CASCADE,null=True)
    post_single_image1  = models.ImageField(upload_to='blog_rasm')
    content_header  = models.TextField(max_length=1000)
    post_single_image2  = models.ImageField(upload_to='blog_rasm')
    content_body    = models.TextField(max_length=1000)
    paragraph   = models.TextField(max_length=500)
    agent       = models.ForeignKey(AgentModel, on_delete=models.CASCADE)
    date        = models.DateField(auto_now_add=True, null=True,blank=True)
    time        = models.TimeField(auto_now_add=True, null=True)
    slug        = models.SlugField(unique=True, blank=True)
    tags        = TaggableManager()
    blog_view = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=80,null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    reply    = models.ForeignKey('self',on_delete=models.SET_NULL, null=True, related_name="replies")
    # parent = models.ForeignKey('self', on_delete=models.CASCADE null=True, blank=True, related_name='replies')

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name

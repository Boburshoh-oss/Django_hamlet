from django.shortcuts import render
from .models import Announcement
from . import utils
# Create your views here.
def index(request):
    announcements=Announcement.objects.all()
    return render(request,'index.html',{'announcements':announcements})
def about(request):
    return render(request,'about.html')
def agents(request):
    return render(request,'agents.html')
def properties(request):
    return render(request,'properties.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    return render(request,'contact.html')
def properties_single(request):
    return render(request,'properties-single.html')
def blog_single(request):
    return render(request,'blog-single.html')
from django.shortcuts import render
from mysite.models import Announcement
from django.contrib.auth.models import User
# Create your views here.
def index(request, username):
    user=User.objects.filter(username=username)
    elonlar = Announcement.objects.filter(foydalanuvchi=request.user)
    return render(request,"personal_area.html", {'elonlar':elonlar, 'user':user})


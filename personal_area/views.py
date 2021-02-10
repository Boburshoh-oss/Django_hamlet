from django.shortcuts import render
from mysite.models import Announcement,Region, District, Status, View

from django.contrib.auth.models import User
import json
from django.core import serializers
from PIL import Image

# Create your views here.
def index(request, username):
    user=User.objects.filter(username=username)
    elonlar = Announcement.objects.filter(author=username)
    return render(request,"personal_area.html", {'elonlar':elonlar, 'user':user})

def add(request, username):
    regions = Region.objects.all()
    json_serializer = serializers.get_serializer("json")()
    districts = json_serializer.serialize(District.objects.all(), ensure_ascii=False)
    statuses = Status.objects.all()
    Property_types = View.objects.all()
    user=User.objects.filter(username=username)

    if request.method == 'POST':
        print("hello world")
        title = request.POST['title']
        region_id = request.POST['region_id']
        district_id = request.POST['district_id']
        location = request.POST['location']
        status_id = request.POST['status_id']
        Property_type_id = request.POST['Property_type_id']
        modum = request.POST['modum']
        image = request.FILES.getlist('image')
        price = request.POST['price']
        Agents = request.POST['agents']
        phone = request.POST['phone']

        announcement = Announcement(
            title=title,
            region_id=region_id,
            district_id=district_id,
            location=location,
            status_id=status_id,
            Property_type_id=Property_type_id,
            modum=modum,
            image=image,
            Price=price,
            Agents=Agents,
            phone=phone,
            author=username
        )
        
        announcement.save()
        print(announcement)
        
    return render(request, 'add.html',
        {
            'regions': regions,
            'districts': districts,
            'Property_types': Property_types,
            'statuses': statuses,
            'user':user
            
        })
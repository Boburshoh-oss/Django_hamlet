from django.shortcuts import render,redirect,get_object_or_404
from mysite.models import Announcement,Region, District, Status, View
from django.contrib.auth.models import User
import json
from django.core import serializers
from PIL import Image
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import ImgForm
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

"""class PersonListView(ListView):
    model = Announcement
    context_object_name = 'people'

def person_create_view(request):
    form=ImgForm()
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('./')
    else:
        form=ImgForm()
    return render(request,'new_add.html',{'form':form})
    

def person_update_view(request,pk):
    person=get_object_or_404(Announcement,pk=pk)
    form=ImgForm(instance=person)
    if request.method=='POST':
        form=ImgForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('person_change',pk=pk)
    else:
        form=ImgForm()
    return render(request,'new_add.html',{'form':form})

def load_cities(request):
    region_id = request.GET.get('region_id')
    districts = District.objects.filter(region_id=region_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': districts})"""
"""def properties(request, username):
    announcement_list=Announcement.object.all().order_by('-date')
    page=request.GET.get('page',1)
    paginator=Paginator(announcement_list,9)
    try:
        announcements=paginator.page(page)
    except PageNotAnInteger:
        announcements=paginator.page(1)
    except EmptyPage:
        announcements=paginator.page(paginator.num_pages)
    region=Region.objects.all()
    district=District.objects.all()
    json_serializer=serializers.get_serializer("json")()
    districts=json_serializer.serialize(District.objects.all(),ensure_ascii=False)
    return render(request,"properties.html",{"announcement":announcements,'regions':region, 'districts':districts})"""

def index(request, username):
    if request.user.is_staff:
        user=User.objects.filter(username=username)
        elonlar = Announcement.objects.filter(author=username)
        return render(request,"personal_area.html", {'elonlar':elonlar, 'user':user})
    else:
        return HttpResponse("nomalum eeee kirish")


def upload(request,username):
    context={}
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_file.name,uploaded_file)
        context['url']=fs.url(name)
    return render(request, 'new_add.html',context)

def upload_book(request,username):
    if request.user.is_staff:
        regions = Region.objects.all()
        json_serializer = serializers.get_serializer("json")()
        districts = json_serializer.serialize(District.objects.all(), ensure_ascii=False)
        if request.method=='POST':
            form=ImgForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('./')
        else:
            form=ImgForm()
        return render(request,'new_add.html',{'form':form, 'regions':regions, 'districts':districts})
    else:
        return HttpResponse("nomalum sahifaga urinish ")





"""def add(request, username):
    regions = Region.objects.all()
    json_serializer = serializers.get_serializer("json")()
    districts = json_serializer.serialize(District.objects.all(), ensure_ascii=False)
    statuses = Status.objects.all()
    Property_types = View.objects.all()
    user=User.objects.filter(username=username)

    if request.method == 'POST' and request.FILES["image"]:
        print("kjnfsefsf")
        image = request.FILES['image']
        fs=FileSystemStorage()
        filename=fs.save(image.name,image)
        url=fs.url(filename)
        title = request.POST['title']
        region_id = request.POST['region_id']
        district_id = request.POST['district_id']
        location = request.POST['location']
        status_id = request.POST['status_id']
        Property_type_id = request.POST['Property_type_id']
        modum = request.POST['modum']
        price = request.POST['price']
        Agents = request.POST['agents']
        phone = request.POST['phone']
        print("shu url",url)
        announcement = Announcement(
            title=title,
            region_id=region_id,
            district_id=district_id,
            location=location,
            status_id=status_id,
            Property_type_id=Property_type_id,
            modum=modum,
            image=url,
            Price=price,
            Agents=Agents,
            phone=phone,
            author=username
        )
        announcement.save()
    return render(request, 'add.html',
        {
            'regions': regions,
            'districts': districts,
            'Property_types': Property_types,
            'statuses': statuses,
            'user':user,            
        })
    """


def success(request): 
    return HttpResponse('successfully uploaded') 

# def announcement_delete(request,id):
#     announcement=get_object_or_404(Announcement,pk=id,author=username)
#     if request.method=="POST":
#         announcement.delete()
#         return render(request,'personal_area.html')
    
# def update_add(request,id):
#     announcement=get_object_or_404(Announcement, pk=id,author=username)
#     form = UpdateAddForm(instance=announcement)
#     if request.method=='POST':
#         form=UpdateAddForm(request.POST,request.FILES,instance=announcement)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         context={'form':form}
#         return render(request,'update_add.html',context)

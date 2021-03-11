from django.shortcuts import render
from .models import Announcement, Region, District, Status, View,Message
from . import utils
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ActorSearchForm
from .search import SearchListView
from .filters import BaseFilter
# Create your views here.

    
def searchPro(request):
    location = self.request.GET.get('keyvalue')  
    status=self.request.GET.get('status')
    PropertyType=self.request.GET.get('PropertType')
    min_price=self.request.GET.get('limit')
    max_price=self.request.GET.get('Max_price')
    agents=self.request.GET.get('Agents')
    beds=self.request.GET.get('Beds')
    bathroom=self.request.GET.get('Bathroom')
    print("eyy kleyapsanmi")
    query_list=Q(location__icontains=location)
    announcement_list=Announcement.objects.filter(query_list).order_by('-date','-time_start')
    print(announcement_list)
    page=request.GET.get('page',1)
    paginator=Paginator(announcement_list,9)
    try:
        announcements=paginator.page(page)
    except PageNotAnInteger:
        announcements=paginator.page(1)
    except EmptyPage:
        announcements=paginator.page(paginator.num_pages)
    
    return render(request,"properties.html",{"object":announcements})
    

class SearchResultsView(ListView):
    model = Announcement
    template_name = 'index.html'
    
    def get_queryset(self): # new
    
        query = self.request.GET.get('keyvalue')  
        status=self.request.GET.get('status')
        PropertyType=self.request.GET.get('PropertType')
        limit=self.request.GET.get('limit')

        
        if query=='' and PropertyType=='' and status=='':
            result_list=Announcement.objects.all()
        elif query!='':
            query_list=Q(location__icontains=query)
            if PropertyType!='':
                query_list=Q(location__icontains=query) & Q(Property_type_id=PropertyType)
            elif status!='':
                query_list=Q(location__icontains=query) & Q(status_id=status)
            result_list=Announcement.objects.filter(query_list).order_by('-date','-time_start')
        elif PropertyType!='':
            query_list=Q(Property_type_id=PropertyType)
            if status!='':
                query_list=Q(Property_type_id=PropertyType) & Q(status_id=status) 
            result_list=Announcement.objects.filter(query_list).order_by('-date','-time_start')
        elif status!='':
            query_list=Q(status_id=status) 
            result_list=Announcement.objects.filter(query_list).order_by('-date','-time_start')
        elif limit!='':
            result_list=Announcement.objects.filter(Price__range=(0,limit)).order_by('-date','-time_start')
        else:
            query_list=Q(location__icontains=query) & Q(Property_type_id=PropertyType) & Q(status_id=status) 
            result_list=Announcement.objects.filter(query_list).order_by('-date','-time_start')
        #result_list=HttpResponse("malumot qani")
        # for i in result_list:
        #     if i=='':
        #         print("malumot yo'q",i)
        #     else:
        #         print("malumot topilmayapti",i)
        return result_list
       

def index(request):
    status=Status.objects.all()
    turlari=View.objects.all()
    announcements=Announcement.objects.all()
    return render(request,'index.html',{'announcements':announcements,'status':status,'turlari':turlari})

    
def about(request):
    return render(request,'about.html')
def agents(request):
    return render(request,'agents.html')



# class SearchResultsPropView(ListView):
#     model = Announcement
#     template_name = 'properties.html'
    
#     def get_queryset(self): # new
#         location = self.request.GET.get('keyvalue')  
#         status=self.request.GET.get('status')
#         PropertyType=self.request.GET.get('PropertType')
#         min_price=self.request.GET.get('limit')
#         max_price=self.request.GET.get('Max_price')
#         agents=self.request.GET.get('Agents')
#         beds=self.request.GET.get('Beds')
#         bathroom=self.request.GET.get('Bathroom')
#         print("eyy kleyapsanmi")
#         print(location)
#         print(stats)
#         print(PropertyType)
#         print(min_price)
#         print(max_price)
#         print(agents)
#         print(beds)
#         print(bathroom)
#         query_list=Q(location__icontains=location) | Q(Property_type_id=PropertyType) | Q(status_id=status) | Q(Agents__icontains=agents)
#         result_list=Announcement.objects.filter(query_list).order_by('-date','-time_start')
#         return result_list



def properties(request):
    location = request.GET.get('keyvalue')  
    status=request.GET.get('prostatus')
    PropertyType=request.GET.get('PropertType')
    min_price=request.GET.get('limit')
    max_price=request.GET.get('Max_price')
    agents=request.GET.get('Agents')
    beds=request.GET.get('Beds')
    bathroom=request.GET.get('Bathroom')
    print("eyy kleyapsanmi")
    print(PropertyType)
    print(min_price)
    print(max_price)
    print(beds)
    print(bathroom)
    print(location)
    print(status)
    print(agents)
    if location or status or PropertyType or min_price or max_price or agents or beds or bathroom:
        # if PropertyType=='' and status=='':
        #     query_list=Q(location__icontains=location)  | Q(Agents=agents) | Q(Price=max_price)
        # elif PropertyType=='':
        #     query_list=Q(location__icontains=location) | Q(status_id=status) | Q(Agents=agents) | Q(Price=max_price)
        # elif status=='':
        #     query_list=Q(location__icontains=location)| Q(Property_type_id=PropertyType) | Q(Agents=agents) | Q(Price=max_price)
        # elif min_price=='':
        #     query_list=Q(location__icontains=location) | Q(status_id=status) | Q(Property_type_id=PropertyType) | Q(Agents=agents) 
        # else:
            # query_list=Q(location__icontains=location) | Q(status_id=status) | Q(Property_type_id=PropertyType) | Q(Agents=agents) | Q(Price=max_price)
        query_list=Q(location__icontains=location) | Q( status_id=status) | Q(Property_type_id=PropertyType) | Q(Agents=agents) | Q(Price=max_price)
        announcement_list=Announcement.objects.filter(query_list).order_by('-date','-time_start')
        page=request.GET.get('page',1)
        paginator=Paginator(announcement_list,9)
        try:
            announcements=paginator.page(page)
        except PageNotAnInteger:
            announcements=paginator.page(1)
        except EmptyPage:
            announcements=paginator.page(paginator.num_pages)
        
        return render(request,"properties.html",{"object":announcements})
    
    announcement_list=Announcement.objects.all().order_by('-date','-time_start')
    page=request.GET.get('page',1)
    paginator=Paginator(announcement_list,9)
    try:
        announcements=paginator.page(page)
    except PageNotAnInteger:
        announcements=paginator.page(1)
    except EmptyPage:
        announcements=paginator.page(paginator.num_pages)
    
    return render(request,"properties.html",{"announcements":announcements})

def properties_single(request,id):
    announcements=get_object_or_404(Announcement,pk=id)
    return render(request,"properties-single.html",{'announcmenets':announcements})

def blog(request):
    return render(request,'blog.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        habar='Name: '+name+'\n'+'email: '+email+'\n'+subject+'\n'+'message: '+message
        send_mail(
            'yangi habar',
            habar,
            'testingemail286@gmail.com',
            ['boburbek_botirov@mail.ru'],
            fail_silently=False
        )
        contact_user=Message(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact_user.save()

    return render(request,'contact.html')

def blog_single(request):
    return render(request,'blog-single.html')
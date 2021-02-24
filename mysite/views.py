from django.shortcuts import render
from .models import Announcement, Region, District, Status, View
from . import utils
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.shortcuts import get_object_or_404
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'



class SearchResultsView(ListView):
    model = Announcement
    template_name = 'index.html'
    

    def get_queryset(self): # new
        
        statuses=Status.objects.all()
        turlari=View.objects.all()
        query = self.request.GET.get('keyvalue')  
        status=self.request.GET.get('status')
        PropertyType=self.request.GET.get('PropertType')
        limit=self.request.GET.get('limit')

        """if PropertyType is None:
            PropertyType=1
        elif status is None:
            status=1"""
        print("query keldimi",query)
        print("status keldimi",status)
        print("narx keldimi ko'rilarchi", limit)
        print("property type keldimi",PropertyType)
        
        
        
        
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
        return result_list
       

def index(request):
    status=Status.objects.all()
    turlari=View.objects.all()
    announcements=Announcement.objects.all()
    return render(request,'index.html',{'announcements':announcements,'status':status,'turlari':turlari})

"""def search(request,username):
    status=Status.objects.all()
    print("shu status",status)
    types=View.objects.all()
    if request.method=='GET':
        stats=request.GET.get('status')
        keyvalue=request.GET.get('keyvalue')
        propertType=request.GET.get('types')
        query=Q(location__icontains=keyvalue) | Q(status__icontains=propertType )
        resultList=Announcement.objects.filter(query).order_by('-date','-time_start')
        print(resultList)
        return render(request,'index.html',{'result_list':resultist,'status':status,'types':types})"""
    
def about(request):
    return render(request,'about.html')
def agents(request):
    return render(request,'agents.html')
def properties(request):
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
    return render(request,'contact.html')

def blog_single(request):
    return render(request,'blog-single.html')
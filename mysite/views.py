from django.shortcuts import render,redirect
from .models import Announcement, Region, District, Status, View,Message,AgentModel
from . import utils
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Q
from django.views.generic import TemplateView, ListView,DetailView
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import ActorSearchForm, UpdateAddForm
from blogs.models import Post
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from operator import attrgetter
from .filters import AnnounFilter
from django.db.models import Max
from datetime import date
# Create your views here.

    
# def searchPro(request):
#     location = self.request.GET.get('keyvalue')  
#     status=self.request.GET.get('status')
#     PropertyType=self.request.GET.get('PropertType')
#     min_price=self.request.GET.get('limit')
#     max_price=self.request.GET.get('Max_price')
#     agents=self.request.GET.get('Agents')
#     beds=self.request.GET.get('Beds')
#     bathroom=self.request.GET.get('Bathroom')
#     print("eyy kleyapsanmi")
#     query_list=Q(location__icontains=location)
#     announcmenets=Announcement.objects.filter(query_list).order_by('-date','-time_start')
    
#     page=request.GET.get('page',1)
#     paginator=Paginator(announcmenets,9)
#     try: 
#         blog_posts=paginator.page(page)
#     except PageNotAnInteger:
#         blog_posts=paginator.page(1)
#     except EmptyPage:
#         blog_posts=paginator.page(paginator.num_pages)
#     print(blog_posts,"malumotlar")
#     return render(request,"properties.html",{'announcements':blog_posts})
    

# class ActorsFilter(BaseFilter):
#     search_fields = {
#         'search_text' : ['location',],
#         # 'search_age_exact' : { 'operator' : '__exact', 'fields' : ['Price'] },
#         # 'search_age_min' : { 'operator' : '__gte', 'fields' : ['Price'] },
#         # 'search_age_max' : { 'operator' : '__lte', 'fields' : ['Price'] },

#     }

# class ActorsSearchList(SearchListView):
#     model = Announcement
#     # paginate_by = 30
#     template_name = "index.html"
#     form_class = ActorSearchForm
#     filter_class = ActorsFilter


def index(request):
    status=Status.objects.all()
    turlari=View.objects.all()
    announcements=Announcement.objects.all()
    posts=Post.objects.all()
    d0 = date(2021, 4, 1)
    d1 = date.today()
    delta = d1 - d0
    return render(request,'index.html',{'announcements':announcements,'status':status,'turlari':turlari,'posts':posts,'delta':delta.days})

    
def about(request):
    return render(request,'about.html')
def agents(request):
    agent=AgentModel.objects.all()
    poster=Announcement.objects.all()
    
    return render(request,'agents.html',{'Agents':agent})


# def agents_single(request):
#     # user=User.objects.filter(username=username)
#     elonlar = Agents.objects.all()
#     own_poster=Announcement.objects.filter()
#     return render(request,"personal_area.html", {'announcements':elonlar})
class AgentDetailView(DetailView):
    model = AgentModel
    template_name = 'agents-single.html'
    def get(self,request,pk):
        announcements = Announcement.objects.filter(Agents = pk)
        agents=AgentModel.objects.filter(id=pk)

        # users_in_group = Group.objects.get(name="agentlar").user_set.all()
        # is_member = request.user in users_in_group
        
        
        announcement_list = Announcement.objects.filter(Agents=pk).order_by('-date')
        page = request.GET.get('page',1)
        paginator = Paginator(announcement_list,3)
        try:
            announcements = paginator.page(page)
        except PageNotAnInteger:
            announcements = paginator.page(1)
        except EmptyPage:
            announcements = paginator.page(paginator,num_pages)
        return render(
            self.request,
            self.template_name,
            {
                'announcements':announcements,
                'Agents':agents
            }
        )

class SearchIndexView(ListView):
    model = Announcement
    template_name = 'index.html'
    
    def get(self,request): # new
        prostatus=Status.objects.all()
        turlari=View.objects.all()
        posts=Post.objects.all()
        query = self.request.GET.get('keyvalue')  
        status=self.request.GET.get('prostatus')
        PropertyType=self.request.GET.get('PropertType')
        limit=self.request.GET.get('limit')
        max_price=self.request.GET.get('max_price')
        
        print(query,"location keldi")
        print(status,'status')
        print(PropertyType,"prop type")
        if query:
            if max_price:
                query_list=Q(location__icontains=query) | Q(Property_type_id=PropertyType) | Q(status_id=status) | Q(Price__range=(0,max_price))
            else:
                query_list=Q(location__icontains=query) | Q(Property_type_id=PropertyType) | Q(status_id=status)

        else:
            if max_price:
                query_list=Q(Property_type_id=PropertyType) | Q(status_id=status) | Q(Price__range=(0,max_price))
            else:
                query_list=Q(Property_type_id=PropertyType) | Q(status_id=status) 

        print(query_list)
        index_result=Announcement.objects.filter(query_list).order_by('-date','-time_start')
        announcements=Announcement.objects.all()
        print(index_result,"zaybal u bu narsa keldimi")
        context = {
            'turlari':turlari,
            'status':prostatus,
            'index_result':index_result,
            'posts':posts,
            'announcements':announcements
        }

        return render(self.request,self.template_name,context)
class SearchResultsView(ListView):
    paginate_by = 6
    model = Announcement
    template_name = 'properties.html'
    
    def get(self,request): # new
        turlari=View.objects.all()
        prostatus=Status.objects.all()
        Agent=AgentModel.objects.all()
        
        title=self.request.GET.get('title')  
        location = self.request.GET.get('keyvalue')  
        
        status=self.request.GET.get('prostatus')
        
        PropertyType=self.request.GET.get('PropertType')
        min_price=self.request.GET.get('min_price',0)
        max_price=self.request.GET.get('max_price',0)
        print(location,"manzil keldimi")
        print(PropertyType,"type keldimi")
        print(status,"statuschi")
        print(max_price,"narxichi")
        if min_price =='':
            min_price=0
        if max_price=='':
            max_price=Announcement.objects.all().aggregate(Max('Price'))
        agents=self.request.GET.get('Agents_id')
        beds=self.request.GET.get('Beds')
        bathroom=self.request.GET.get('Bathroom')
    


    
        if title and location=='':
            if min_price!=0 or max_price!=Announcement.objects.all().aggregate(Max('Price')):
                if max_price==Announcement.objects.all().aggregate(Max('Price')):
                    query_list=(Q(title__icontains=title)|Q(Price__range=(min_price,max_price['Price__max']))|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
                    print(query_list,"max yo'q")
                else:
                    query_list=(Q(title__icontains=title)|Q(Price__range=(min_price,max_price))|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
                    print(query_list,"max bor")
            else:
                query_list=(Q(title__icontains=title)|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
        elif location and title=='':
            if min_price!=0 or max_price!=Announcement.objects.all().aggregate(Max('Price')):
                if max_price==Announcement.objects.all().aggregate(Max('Price')):
                    query_list=(Q(location__icontains=location)|Q(Price__range=(min_price,max_price['Price__max']))|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
                    print(query_list,"title yo'q")
                else:
                    query_list=(Q(location__icontains=location)|Q(Price__range=(min_price,max_price))|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
                    print(query_list,"title bor")
            else:
                query_list=(Q(location__icontains=location)|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
        elif title and location:
            if min_price!=0 or max_price!=Announcement.objects.all().aggregate(Max('Price')):
                if max_price==Announcement.objects.all().aggregate(Max('Price')):
                    query_list=(Q(title__icontains=title)|Q(location__icontains=location)|Q(Price__range=(min_price,max_price['Price__max']))|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
                    print(query_list,"title location  bor")
                else:
                    query_list=(Q(title__icontains=title)|Q(location__icontains=location)|Q(Price__range=(min_price,max_price))|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
                    print(query_list,"max bor")
            else:
                query_list=(Q(title__icontains=title)|Q(location__icontains=location)|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
        elif title=='' and location=='':
            if min_price!=0 or max_price!=Announcement.objects.all().aggregate(Max('Price')):
                if max_price==Announcement.objects.all().aggregate(Max('Price')):
                    query_list=(Q(Price__range=(min_price,max_price['Price__max']))|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
                    print(query_list,"max yo'q")
                else:
                    query_list=(Q(Price__range=(min_price,max_price))|Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
                    print(query_list,"max bor")
            else:
                query_list=(Q(Property_type_id=PropertyType)|Q(status_id=status)|Q(Agents_id=agents))
        
        print(query_list,"keldimi querylist")
        result_list=Announcement.objects.filter(query_list).order_by('-date','-time_start')
        paginator = Paginator(result_list, self.paginate_by)
        page = request.GET.get('page',1)
        
        try:
            result_list = paginator.page(page)
        except PageNotAnInteger:
            result_list = paginator.page(1)
        except EmptyPage:
            result_list = paginator.page(paginator,num_pages)
        
        
        context = {
            'turlari':turlari,
            'status':prostatus,
            'Agents':Agent,
            'blog_posts':result_list

        }
        return render(self.request,self.template_name, context)
    # def get_context_data(self, **kwargs):
    #     context = super(SearchResultsView,self).get_context_data(**kwargs)
    #     context.update({
    #         'turlari':View.objects.all(),
    #         'status':Status.objects.all()
    #     })
    #     return context
def get_blog_queryset(query=None,PropertType=None,status=None,agent=None):
    queryset = []

    queries=query.split(" ") 
    print(queries,"nima shu necha kelyapti")
    print(PropertType,"endi bu nima")
    print(status,"status keldi")
    print(agent,'agent keldi')
    # if PropertType!='':
    # try:
    posts = Announcement.objects.filter(Q(location__icontains=query)|Q(Property_type_id=PropertType)|Q(status_id=status)|Q(Agents_id=agent)).distinct()
    # except ValueError:
    #     posts = Announcement.objects.filter(Q(location__icontains=query)).distinct()
    # else:
    #     posts = Announcement.objects.filter(Q(location__icontains=query)).distinct()
    for post in posts:
    	queryset.append(post)
    # for q in queries:
    #     if PropertType!='':
	#         posts = Announcement.objects.filter(Q(location__icontains=q)|Q(Property_type_id=PropertType)).distinct()
    #     else:
    #         posts = Announcement.objects.filter(Q(location__icontains=q)).distinct()
	#     for post in posts:
	# 	    queryset.append(post)

    return list(set(queryset))



def properties(request):
    context={}
    # query=""
    # PropertType=""
    # status=""
    # agent=""
    
    # query=request.GET.get('keyvalue','')
    # PropertType=request.GET.get('PropertType',None)
    # status=request.GET.get('prostatus',None)
    # agent=request.GET.get('Agents_id',None)
    # context['query']=str(query)
    # context['PropertType']=str(PropertType)
    # context['status']=str(status)
    # context['agent']=str(agent)

    turlari=View.objects.all()
    prostatus=Status.objects.all()
    agents=AgentModel.objects.all()
    # blog_posts=sorted(get_blog_queryset(query,PropertType,status,agent),key=attrgetter('date','time_start'),reverse=True)
    blog_posts=Announcement.objects.all().order_by('-date','-time_start')
    page=request.GET.get('page',1)
    paginator=Paginator(blog_posts,6)
    try:
        blog_posts=paginator.page(page)
    except PageNotAnInteger:
        blog_posts=paginator.page(1)
    except EmptyPage:
        blog_posts=paginator.page(paginator.num_pages)
    context['announcements']=blog_posts
    context['turlari']=turlari
    context['status']=prostatus
    context['Agents']=agents
    return render(request,"properties.html",context)


def propertiesFilter(request):
    context={}
    filtered_announ=AnnounFilter(
        request.GET,
        queryset=Announcement.objects.all()
    )
    context['filtered_announ']=filtered_announ.qs

    return render(request,'properties.html',context=context)


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
        # try:
        send_mail(
        'yangi habar',
        habar,
        'boburbekbotirov868@gmail.com',
        ['boburbek_botirov@mail.ru'],
        fail_silently=False
        )
        # except:
        #     return HttpResponse("iltimos internetga ulanganingizni tekshiring")
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

def announcement_delete(request,id):
    announcement=get_object_or_404(Announcement,pk=id,author=request.user)
    if request.method=="POST":
        print("post kelyaptimi")
        announcement.delete()
        return redirect("../../personalE")
    
def update_add(request,id):
    announcement=get_object_or_404(Announcement, pk=id,author=request.user)
    form = UpdateAddForm(instance=announcement)
    if request.method == 'POST':
        form=UpdateAddForm(request.POST,request.FILES,instance=announcement)
        if form.is_valid():
            form.save()
            return redirect('../../personalE')
        context={'form':form}
        return render(request,'update_add.html',context)
    else:
        return render(request,'update_add.html',{'form':form})

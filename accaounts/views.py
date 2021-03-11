from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from .forms import loginForm, registerForm
from django.http import HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse
import json


MAILCHIMP_API_KEY=settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER=settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_MAIL_LIST_ID=settings.MAILCHIMP_MAIL_LIST_ID
api_url=f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0/'
members_endpoint=f'{api_url}/lists/{MAILCHIMP_MAIL_LIST_ID}/members'

# def subscribe(email):
#     data={
#         "email_address":email,
#         'status':'subscribed'
#     }
#     r=request.POST(
#         members_endpoint,
#         auth=("",MAILCHIMP_API_KEY),
#         data=json.dumps(data)
#     )
#     retrun r.status_code, r.json()

# def email_list_sign_up(request):
#     form=EmailSignupForm(request.POST or None)
#     if request.method=="POST":
#         if form.is_valid():
#             email_signup_qs=Signup.objects.filter(email=form.instance.email)
#             if email_signup_qs.exists():
#                 messages.info(request,"You are already subscribed")
#             else:
#                 subscribe(form.instance.email)
#                 form.save()
#     return HttpResponseRedirect(request,META.get("HTTP_REFERER"))


# from django.http import HttpResponse, JsonResponse
# from .models import Subscribe
# from .utils import SendSubscribeMail

# def subscribe(request):
#     if request.method == 'POST':
#         email = request.POST['email_id']
#         email_qs = Subscribe.objects.filter(email_id = email)
#         if email_qs.exists():
#             data = {"status" : "404"}
#             return JsonResponse(data)
#         else:
#             Subscribe.objects.create(email_id = email)
#             SendSubscribeMail(email) # Send the Mail, Class available in utils.py
            
#     return HttpResponse("/")
# def base(request):
#     form=EmailSignupForm()
#     return render(request,'base.html',{'form':form})
# Create your views here.
def sign_up(request):
    if request.method=='POST':
        register_form=registerForm(request.POST)
        if register_form.is_valid():
            first_name=register_form.cleaned_data['first_name']
            last_name=register_form.cleaned_data['last_name']
            email=register_form.cleaned_data['email']
            username=register_form.cleaned_data['username']
            password1=register_form.cleaned_data['password1']
            password2=register_form.cleaned_data['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "foydalanuvchi mavjud, qayta urining")
                return redirect('sign_up')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email avval ro'yhatdan o'tgan")
                return redirect('sign_up')
            else:
                user = User.objects.create_user(
                        email = email,
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        password = password1
                    )
                user.save()
                
                
                
        else:
            messages.info(request,"parollar bir xilligini tekshiring")
            return redirect('sign_up')
        return redirect("../" + username)
    else:
        register_form=registerForm()
        return render(request,'accaounts/sign_up.html',{'form':register_form})
def sign_in(request):
    if request.method=='POST':
        login_form=loginForm(request.POST)
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            #email=request.POST['email']
            user=auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request,user)
                
                return redirect("../"+username)
            else:
                messages.info(request, "Username yoki parol xato, Ro'yhatdan o'tganingizni tekshiring!")
                return redirect("sign_in")
    else:
        login_form=loginForm()
        return render(request, 'accaounts/sign_in.html',{'form':login_form})
def sign_out(request):
    auth.logout(request)
    return redirect('/')


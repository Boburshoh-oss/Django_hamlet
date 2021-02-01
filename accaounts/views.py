from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages 
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from .forms import loginForm, registerForm

# Create your views here.
def sign_up(request):
    if request.method=='POST':
        register_form=registerForm(request.POST)
        if register_form.is_valid():
            first_name=register_form.cleaned_data['first_name']
            last_name=register_form.cleaned_data['last_name']
            email=register_form.cleaned_data['password1']
            username=register_form.cleaned_data['username']
            password1=register_form.cleaned_data['password1']
            password2=register_form.cleaned_data['password2']
        #first_name=request.POST['first_name']
        #last_name=request.POST['lasst_name']
        #username=request.POST['username']
        #email=request.POST['email']
        #password1=request.POST['password1']
        #password2=request.POST['password2']


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
from django.urls import path
from . import views
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 
from mysite import views as viyu

  
urlpatterns = [ 
    path('success', views.success, name = 'success'),
    path('',views.index, name="personalE"),
    path('new_add',views.upload_book, name='new_add'),
] 
  




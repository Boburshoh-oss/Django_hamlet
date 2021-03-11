from django.urls import path
from . import views
from django.contrib import admin 
from django.conf import settings 
from django.conf.urls.static import static 


  
urlpatterns = [ 
    path('success', views.success, name = 'success'),
    path('',views.index, name="personalE"),
    #path('add',views.add, name='add'),
    path('new_add',views.upload_book, name='new_add'),
    
    #path('add/', views.person_create_view, name='person_add'),
    #path('<int:pk>/', views.person_update_view, name='person_change'),
    #path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX
] 
  




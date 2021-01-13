
from . import views
from django.urls import path
from . import utils

urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('agents',views.agents, name='agents'),
    path('properties',views.properties, name='properties'),
    path('blog',views.blog, name='blog'),
    path('contact',views.contact, name='contact'),
    path('properties-single',views.properties_single),

    path('blog-single',views.blog_single),
]

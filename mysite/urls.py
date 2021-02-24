
from . import views
from django.urls import path
from . import utils
from personal_area.views import upload_book
from .views import HomePageView, SearchResultsView
urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('agents',views.agents, name='agents'),
    path('properties',views.properties, name='properties'),
    path('blog',views.blog, name='blog'),
    path('contact',views.contact, name='contact'),
    #path('properties-single',views.properties_single),
    path('blog-single',views.blog_single),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('properties-single/<int:id>/',views.properties_single, name='properties-single'),
    #path('search',views.search, name='search')
]

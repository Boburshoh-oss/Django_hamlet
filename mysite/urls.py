
from . import views
from django.urls import path
from . import utils
from personal_area.views import upload_book
from .views import  SearchResultsView
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
    path('properties-single/<int:id>/',views.properties_single, name='properties-single'),
    path('searchPro',views.searchPro,name="searchPro" )
    # path('', PropertiesPageView.as_view(), name='Pro'),
    # path('prosearch', SearchResultsPropView.as_view(), name='Pro_search_results'),
    
    
    #path('search',views.search, name='search')
]

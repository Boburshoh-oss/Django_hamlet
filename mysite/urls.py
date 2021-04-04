
from . import views
from django.urls import path
from . import utils
from personal_area.views import upload_book
from .views import  AgentDetailView,SearchResultsView,propertiesFilter,SearchIndexView
urlpatterns = [
    path('', views.index, name='index'),
    path('about',views.about, name='about'),
    path('agents',views.agents, name='agents'),
    path('properties',views.properties, name='properties'),
    path('blog',views.blog, name='blog'),
    path('contact',views.contact, name='contact'),
    path('blog-single',views.blog_single),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('searchIndex/',SearchIndexView.as_view(),name="searchIndex"),
    path('properties-single/<int:id>/',views.properties_single, name='properties-single'),
    # path('searchPro',views.searchPro,name="searchPro"),
    path('delete/<int:id>/',views.announcement_delete,name='delete'),
    path('update-add/<int:id>/',views.update_add, name='update_add'),
    path('agent-single/<int:pk>/',views.AgentDetailView.as_view(),name='agent-single'),
    
]

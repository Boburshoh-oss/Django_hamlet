from django.urls import path
from . import views



    

urlpatterns = [
    path('blog-single/<int:id>/',views.blog_single, name='blog-single'),
    path('blog/',views.blog, name='blog'),
    path('Categories/<int:pk>', views.BlogCategoriesDetailView.as_view(), name="categories-detail"),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
    path("post-search/",views.SearchResultsPropView.as_view(),name="search"),
    # path('comment/',views.CommentDetailView.as_view(),name="comment"),
    path('<int:year>/<int:month>/',
         views.ArticleMonthArchiveView.as_view(month_format='%m'),
         name="post_archive_month"),
]
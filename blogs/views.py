
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404,HttpResponseRedirect
from django.contrib.auth.models import User, Group
from .models import Post, Post_categorie,Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import DetailView, ListView
from taggit.models import Tag
from .forms import PostForm,CommentForm
from django.template.defaultfilters import slugify
from hitcount.views import HitCountDetailView
from django.views.generic.dates import MonthArchiveView



def blog_single(request,id):
    posts = get_object_or_404(Post, pk=id)
    blog_post = Post.objects.all().order_by('-date','-time')[:5]
    post = Tag.objects.all()
    categories = Post_categorie.objects.all()
    user=User.objects.all()
    post_object=Post.objects.get(id=id)
    post_object.blog_view = post_object.blog_view + 1
    post_object.save()

    template_name = 'blog-single.html'
    # post = get_object_or_404(Post, slug=slug)
    # comments = posts.comments.filter(active=True)
    comments = Comment.objects.filter(post=posts,reply=None)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            reply_id = request.POST.get('comment_id')
            comment_qs = None
            
            if reply_id:
                comment_qs= Comment.objects.get(id=reply_id)

            new_comment = comment_form.save(commit=False)
            new_comment.reply=comment_qs
            # Assign the current post to the comment
            new_comment.author=request.user
            new_comment.post = posts
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(request.path)
            
    else:
        comment_form = CommentForm()
        # return render(request, 'blog-single.html', {'contributeForm': comment_form})
    # users_in_group = Group.objects.get(name="Admin").user_set.all()
    # is_member = request.user in users_in_group
    context = {
        'posts': posts,
        # 'is_member':is_member,
        'blog_post':blog_post,
        'categories':categories,
        'post':post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'user':user
    }
    return render(request, template_name,context)


# class CommentDetailView(HitCountDetailView):
#     model = Comment
#     template_name = "blog-single.html"
#     slug_field="slug"
#     count_hit=True

#     form=CommentForm

#     def post(self,request,*args, **kwargs):
#         form=CommentForm(request.POST)
#         if form.is_valid():
#             post=self.get_object()
#             form.instance.user=request.user
#             form.instance.post=post
#             form.save()
#             print(form,"voshe kemayapti")
#             return redirect(reverse("post",kwargs={
#                 'slug':post.slug
#             }))
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = self.form
    #     return context
    

def blog(request):
    posts = Post.objects.all().order_by('-date','time')
    # users_in_group = Group.objects.get(name="Admin").user_set.all()
    # is_member = request.user in users_in_group
 
    post_list = Post.objects.all().order_by('-date')
    page = request.GET.get('page',1)
    paginator = Paginator(post_list,4)
    # comments_count=posts.Comment_set.all()

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator,num_pages)
    return render(request, "blog.html", {'posts': posts})


class SearchResultsPropView(ListView):
    model = Post
    template_name = 'blog.html'
    
    def get_queryset(self): # new
        query = self.request.GET.get('keyvalue')  
        query_list=Q(content_header__icontains=query) | Q(content_body__icontains=query) | Q(title__icontains=query)
        result_list=Post.objects.filter(query_list).order_by('-date')
        return result_list
# class BlogView(DetailView):
#     model = Post
#     def get_object(self):
#         
# def blog_post(request,id):
#     #your code
#     blog_object=Post.objects.get(id=id)
#     blog_object.blog_views=blog_object.blog_views+1
#     blog_object.save()
#     print(blog_object,"nima shu object")
#     return render(request,'blog.single',{'context':blog_object})

class BlogCategoriesDetailView(DetailView):
    model = Post
    template_name = 'blog.html'

    def get(self,request,pk):
        # obj = super().get_object()
        # obj.blog_view += 1
        # obj.save()
        # print(obj,"shu object ")
        

        posts = Post.objects.filter(categories = pk)
        
        # users_in_group = Group.objects.get(name="Admin").user_set.all()
        # is_member = request.user in users_in_group

        blog_list = Post.objects.filter(categories=pk).order_by('-date')
        page = request.GET.get('page',1)
        paginator = Paginator(blog_list,4)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator,num_pages)

        return render(
            self.request,
            self.template_name,
            {
                'posts':posts,
                'obj':obj
            }
        )



def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = Post.objects.filter(tags=tag)
    context = {
        'posts':posts,
    }
    return render(request, 'blog.html', context)

class ArticleMonthArchiveView(MonthArchiveView):
    queryset = Post.objects.all()
    date_field = "posted"
    allow_future = True

# def home_view(request):
#     posts = Post.objects.order_by('-date')
#     # Show most common tags 
#     common_tags = Post.tags.most_common()[:4]
#     form = PostForm(request.POST)
#     if form.is_valid():
#         newpost = form.save(commit=False)
#         newpost.slug = slugify(newpost.title)
#         newpost.save()
#         # Without this next line the tags won't be saved.
#         form.save_m2m()
#     context = {
#         'posts':posts,
#         'common_tags':common_tags,
#         'form':form,
#     }
#     return render(request, 'new_add.html', context)
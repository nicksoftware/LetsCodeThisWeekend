from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,get_object_or_404
from .models import Post
from courses.models import Course,Category


def blog(request):
    posts = Post.objects.order_by('-pub_date').filter(is_published=True)
    categories = Category.objects.all()[:4]
    courses = Course.objects.order_by('-pub_date').filter(is_published=True)
    context ={
        'posts':posts,
        'categories': categories,
        'courses':courses
    }

    return render(request, 'blog/index.html',context)

def  blog_detail(request, post_id):
    
    post = get_object_or_404(Post,pk=post_id)
    context = {
        'post':post
    }
    return render(request,'blog/blog_detail.html',context)


def blog_search(request):
    return render(request, 'blog/search.html')

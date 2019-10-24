from django.shortcuts import render
from blog.models import Post
from courses.models import Course
# Create your views here.
def index(request):
    courses = Course.objects.order_by('-pub_date').filter(is_published=True)[:4]
    
    posts = Post.objects.order_by('-pub_date').filter(is_published=True)[:3]
    context = {
        'courses':courses,
        'posts':posts
    }
    return render(request, 'pages/index.html',context)

def about(request):
    context = {
        
    }
    return render(request, 'pages/about.html',context)
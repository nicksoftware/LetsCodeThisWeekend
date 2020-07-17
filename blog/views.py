from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,get_object_or_404
from .models import Post, Comment
from courses.models import Course,Category
from .forms import CommentForm


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
    form = CommentForm()
    post = get_object_or_404(Post,pk=post_id)
    context = {
        'post':post,
        'form': form,
     
    }
    if request.method == "POST":
        form = CommentForm(request.POST)

        # if request.session.get('has_commented', False):
        #     messages.error(request,  'You have already commented.')
        #     return render(request,'blog/blog_detail.html',context)
        # if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        request.session['has_commented'] = True
        return render(request,'blog/blog_detail.html',context)
        
  

    return render(request,'blog/blog_detail.html',context)


def blog_search(request):
    return render(request, 'blog/search.html')




def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
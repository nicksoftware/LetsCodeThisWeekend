from django.shortcuts import render

from courses.models import Course
# Create your views here.
def index(request):
    courses = Course.objects.order_by('-pub_date').filter(is_published=True)
    context = {
        'courses':courses
    }
    return render(request, 'pages/index.html',context)
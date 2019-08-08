from django.shortcuts import render,redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.contrib.auth.models import User, auth
from courses.models import Course
def register(request):
    if request.method == 'POST':
        #register user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #Validation
        #password first
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username already taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email already registered')
                    return redirect('register')
                else:
                    #looks Good
                    user = User.objects.create_user(username=username,email=email, password=password, first_name=first_name, last_name=last_name)
                    #login after register
                    # auth.login(request, user)
                    # messages.success(request, 'you are now logged in ')
                    # return redirect('/')
                    user.save()
                    messages.success(request, 'You have successfully registered an account and you can now login')
                    return redirect('login')
        else:
            #show error
            messages.error(request,'passwords do not match')
            return redirect('register')

        return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        #login user
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        #validation
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def dashboard(request):
    courses = Course.objects.order_by('-pub_date').filter(is_published=True)
    paginator = Paginator(courses, 6)
    page = request.GET.get('page')
    paged_courses = paginator.get_page(page)
    context = {
       'courses':courses,
       'courses':paged_courses,
    }
    return render(request, 'dashboard.html',context)

def logout(request):
    if request.method == 'POST':
        #logout
        auth.logout(request)
        messages.success(request, 'You have successfully logged out')
        return redirect('index')
def settings(request):
    return render(request, 'accounts/settings.html')
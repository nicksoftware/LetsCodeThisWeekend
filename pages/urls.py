from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('courses/',include('courses.urls'),name="courses"),
    path('',include('accounts.urls'),name="accounts"),
    path('about/',views.about, name="about")

]
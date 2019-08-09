
from django.urls import path 
from . import views

urlpatterns = [
    path('courses', views.course_list, name='courses'),
    path('<int:course_pk>/<int:step_pk>/',views.step_detail),
    path('<int:course_id>/', views.detail_view,name = 'detail'),
    path('search/', views.search, name='search'),

]

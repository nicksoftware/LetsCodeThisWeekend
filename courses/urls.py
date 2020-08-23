
from django.urls import path 
from . import views

urlpatterns = [
    path('courses', views.course_list, name='courses'),
    path('Development', views.category_list, name='category'),
    path('<int:course_pk>/<int:step_pk>/<int:tut_pk>',views.tutorial_detail,name='section'),
    path('<int:course_id>/', views.detail_view,name = 'detail'),
    path('search/', views.search, name='search'),

]


from django.urls import path 

from . import views

urlpatterns = [
    path('', views.course_list),
    path('<int:course_id>', views.detail_view,name = 'detail'),
    path('search/', views.search, name='search')
]

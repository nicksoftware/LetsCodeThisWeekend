from django.contrib import admin
from .models import Course
from .models import Step
from .models import Instructor


class StepInline(admin.StackedInline):
    model = Step

class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]
    list_display = ('id', 'title','category', 'is_published', 'price', 'pub_date')
    list_editable = ('is_published','category')
    list_display_links = ('id', 'title')

    list_per_page = 25
    
admin.site.register(Course,CourseAdmin)
admin.site.register(Instructor)
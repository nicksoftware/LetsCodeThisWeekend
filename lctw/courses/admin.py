from django.contrib import admin
from .models import Course
from .models import Step
from .models import Instructor

# Register your models here.

class StepInline(admin.StackedInline):
    model = Step

class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]
    
admin.site.register(Course,CourseAdmin)
admin.site.register(Instructor)
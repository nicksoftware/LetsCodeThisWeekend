from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Link,
    Skill,
    Category,
    Instructor,
    Course,
    Tutorial,
    Step
)


class LinkAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


class SkillAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


class CategoryAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


class InstructorAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


class TutorialAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


class StepAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Link, LinkAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Step, StepAdmin)

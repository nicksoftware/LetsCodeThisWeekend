from django.contrib import admin
from .models import Post
from .models import Story


class StoryInline(admin.StackedInline):
    model = Story

class PostAdmin(admin.ModelAdmin):
    inlines = [StoryInline,]
    list_display = ('id', 'title','category', 'is_published', 'pub_date')
    list_editable = ('is_published','category')
    list_display_links = ('id', 'title')

    list_per_page = 25




admin.site.register(Post,PostAdmin)

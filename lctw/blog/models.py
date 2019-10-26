from django.db import models
from datetime import datetime
from courses.models import Category
from ckeditor.fields import RichTextField

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    pub_date = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    timestomp = models.DateTimeField(auto_now_add=True)
    main_image = models.ImageField(upload_to='images/blog/%Y/%m/%d')
    content = RichTextField()
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Story(models.Model):
    title = models.CharField(max_length=255)
    image =models.ImageField(upload_to='images/blog/%Y/%m/%d',blank=True)
    content = models.TextField()
    order = models.IntegerField(default=0)
    Course = models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    author = models.CharField('Name',max_length=255)
    text = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
from django.db import models

from courses.models import Category

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default="")
    summary = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    main_image = models.ImageField(upload_to='images/blog/%Y/%m/%d')
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

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


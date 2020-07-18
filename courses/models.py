from django.conf import settings
from django.db import models
from embed_video.fields import EmbedVideoField

User = settings.AUTH_USER_MODEL

# Create your models here.
class Link(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    url = models.ManyToManyField(Link, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/skills/', null=True)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/categories/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


class Course(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/courses/')
    publish_date =  models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Tutorial(models.Model):
    title = models.CharField(max_length=100)
    video = EmbedVideoField()
    external_links = models.ManyToManyField(Link, related_name='link', blank=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    promo_video = EmbedVideoField()
    tutorials = models.ManyToManyField(Tutorial, related_name='tutorial')
    description = models.TextField()

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title


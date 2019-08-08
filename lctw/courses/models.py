from django.db import models

# Create your models here.
class Instructor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    languages = models.CharField(max_length=200)
    bio = models.TextField()

class Course(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    price = models.IntegerField(default=0)
    description = models.TextField()
    pub_date =  models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.title




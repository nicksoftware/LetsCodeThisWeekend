from django.db import models
# Create your models here.
class Instructor(models.Model):
    name =models.ForeignKey('auth.User',on_delete=models.CASCADE)
    SKILLS = [
    ('FE', 'Front-end'),
    ('BE', 'Back-end'),
    ('FS', 'Full-Stack'),
    ('IT', 'IT-Specialist'),
]
    skills = models.CharField(max_length=2, choices=SKILLS,blank=True)
    bio = models.TextField()
    
    def __str__(self):
        return self.name.username

class Category(models.Model):
    title = models.CharField(max_length=30,default="")
    description = models.TextField()

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT,default="")
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

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.title




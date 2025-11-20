from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length= 50)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=50)
    context = models.TextField(blank=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%M/%d')
    is_bool = models.BooleanField(default=0)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
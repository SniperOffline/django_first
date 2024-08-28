from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length = 255)
    def __str__(self):
        return self.title

class Blog(models.Model):
    title       = models.CharField(max_length=255)
    content     = models.TextField()
    author      = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blogs')
    category    = models.ForeignKey(Category, on_delete = models.CASCADE, related_name= 'blogs')
    created_at  = models.DateTimeField(auto_now_add = True)
    updated_at  = models.DateTimeField(auto_now = True)
    poster      = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    content     = models.TextField()
    author      = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'comments')
    blog        = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name = 'comments')
    created_at  = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.content
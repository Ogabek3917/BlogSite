from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="photos/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):          
        return self.title





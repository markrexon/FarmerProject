from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.base import ModelState
from django.utils import timezone
from django.urls import reverse


class BlogPost(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, blank=True,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    image_header=models.ImageField(null=True,blank=True,upload_to="images/")
    body = models.TextField()
    post_date=models.DateField(auto_now_add=True)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("blogpost:article-detail", args=(str(self.id)))

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/")
    

    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    post=models.ForeignKey(BlogPost,related_name="comments", on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    message = models.TextField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.email
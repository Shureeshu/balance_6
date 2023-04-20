from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    select1_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_post')
    select1_content = models.TextField()
    img1 = models.ImageField(blank=True, upload_to='images1/')
    select2_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_post')
    select2_content = models.TextField()
    img2 = models.ImageField(blank=True, upload_to='images2/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

# class PostImage(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     img1 = models.ImageField(blank=True, upload_to='images1/')
#     img2 = models.ImageField(blank=True, upload_to='images2/')

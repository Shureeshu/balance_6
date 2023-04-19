from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=80)
    select1_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select1_post')
    select1_content = models.TextField()
    select2_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='select2_post')
    select2_content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
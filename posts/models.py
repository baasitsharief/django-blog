from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='posts_post')
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now(), blank = True)


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Tweet(models.Model):
    tweet_title = models.CharField(max_length=200)
    tweet_description = models.TextField(max_length=5000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=100)
    published = models.DateField()
    
    def __str__(self):
        return self.tweet_title



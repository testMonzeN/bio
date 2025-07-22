from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from datetime import date, timedelta
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)    
    join_to_github = models.CharField(max_length=255, null=True, blank=True)

    count_projects = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('bio', kwargs={'pk': self.pk})

class Link(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name
    
class Icon(models.Model):
    icons = {
        'shop': 'fas fa-shopping-cart',
        'blog': 'fas fa-blog',
        'portfolio': 'fas fa-globe',
        'game': 'fas fa-gamepad',
        'other': 'fas fa-question',
    }
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, choices=icons.items())

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    type_icon = models.ForeignKey(Icon, on_delete=models.CASCADE, null=True, blank=True)
    links = models.ForeignKey(Link, on_delete=models.CASCADE, null=True, blank=True)   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
    

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    time = models.TimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('music_detail', kwargs={'pk': self.pk})


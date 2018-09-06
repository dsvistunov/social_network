from django.db import models
from django.contrib.auth.models import AbstractUser
from src import settings


class SocNetUser(AbstractUser):
    date_birth = models.DateField(
        verbose_name='Date of birth',
        null=True, blank=True
    )
    location = models.CharField(max_length=30)
    facebook = models.CharField(max_length=30)
    bio = models.TextField()


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(blank=True, null=True)
    public = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)


class Dislike(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)

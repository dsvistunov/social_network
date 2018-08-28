from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	user = models.ForeignKey(User)
	title = models.CharField(max_length=255)
	body = models.TextField()
	image = models.ImageField(blank=True, null=True)
	public = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

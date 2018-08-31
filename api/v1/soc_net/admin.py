from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import SocNetUser, Post, Like, Dislike


admin.site.register(SocNetUser, UserAdmin)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Dislike)

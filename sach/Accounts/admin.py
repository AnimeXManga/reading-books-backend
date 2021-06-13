from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User


class PostAdmin(admin.ModelAdmin):
    list_display = ['id','user']

admin.site.register(Profile, PostAdmin)
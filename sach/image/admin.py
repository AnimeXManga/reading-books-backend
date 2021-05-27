from django.contrib import admin

from .models import Hinh

class Post(admin.ModelAdmin):
    list_display = ['id', 'hinh']

admin.site.register(Hinh,Post)
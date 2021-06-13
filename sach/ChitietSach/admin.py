from django.contrib import admin
from .models import Sach, Chuong, Tacgia, Danhmuc, Theloai, Comment
# from .models import Sach, Chuong, Tacgia, Danhmuc, Theloai

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'tieude', 'danhmuc', 'theloai', 'tacgia', 'ngaydang']
    search_fields = ['tieude']


class PostAdminChuong(admin.ModelAdmin):
    list_display = ['id', 'sochuong', 'tieude']
    search_fields = ['sochuong']

admin.site.register(Sach, PostAdmin)
admin.site.register(Chuong, PostAdminChuong)
admin.site.register(Comment)
admin.site.register(Tacgia)
admin.site.register(Danhmuc)
admin.site.register(Theloai)


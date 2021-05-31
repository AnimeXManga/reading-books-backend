from django.contrib import admin
from .models import Sach, Chuong, Tacgia, Danhmuc, Theloai, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','tieude','danhmuc','theloai','tacgia','ngaydang']
    search_fields = ['tieude']


class CommentInline(admin.StackedInline):
    model = Comment

class PostAdminChuong(admin.ModelAdmin):
    list_display = ['id','sochuong', 'tieude']
    search_fields = ['sochuong']
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'chuong', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Sach, PostAdmin)
admin.site.register(Chuong, PostAdminChuong)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tacgia)
admin.site.register(Danhmuc)
admin.site.register(Theloai)

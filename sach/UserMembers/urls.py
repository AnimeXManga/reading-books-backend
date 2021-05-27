from django.urls import path

from . import views
app_name = 'UserMembers'
urlpatterns = [
    path('register/', views.DangkyThanhvien.as_view(), name="dangky"),
    path('login/', views.DangnhapThanhvien.as_view(), name="dangnhap"),
]

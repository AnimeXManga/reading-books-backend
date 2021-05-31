from django.urls import path
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include

from . import views

router = DefaultRouter()
router.register('sach-danhmuc', views.SachDanhmucViewset, basename='sach-danhmuc')
router.register('chuong', views.ChuongViewset, basename='chuong')
router.register('sach-theloai', views.SachTheloaiViewset, basename='sach-theloai')


urlpatterns = [
	url('', include(router.urls)),
	path('api-overview/', views.apiOverview, name="api-overview"),

	path('api-sach-list/', views.taskListSach, name="sach-list"),
	path('api-sach-detail/<str:pk>/', views.taskDetailSach, name="sach-detail"),
	path('api-sach-delete/<str:pk>/', views.taskDeleteSach, name="sach-delete"),

	path('api-chuong-list/', views.taskListChuong, name="chuong-list"),
	path('api-chuong-detail/<str:pk>/', views.taskDetailChuong, name="chuong-detail"),
	path('api-chuong-delete/<str:pk>/', views.taskDeleteChuong, name="chuong-delete"),

	path('api-danhmuc-list/', views.taskListDanhmuc, name="danhmuc-list"),
	path('api-danhmuc-detail/<str:pk>/', views.taskDetailDanhmuc, name="danhmuc-detail"),
	path('api-danhmuc-delete/<str:pk>/', views.taskDeleteDanhmuc, name="danhmuc-delete"),

	path('api-theloai-list/', views.taskListTheloai, name="theloai-list"),
	path('api-theloai-detail/<str:pk>/', views.taskDetailTheloai, name="theloai-detail"),
	path('api-theloai-delete/<str:pk>/', views.taskDeleteTheloai, name="theloai-delete"),

	path('<int:pk>/', views.post_detail, name='post_detail')
]

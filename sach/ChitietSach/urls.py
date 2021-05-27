from django.urls import path

from . import views

"""
urlpatterns = [
    path('api-sach', views.ListCreateViewSach.as_view()),
    path('api-chuong', views.ListCreateViewChuong.as_view()),
    path('api-sach/<int:pk>', views.UpdateDeleteViewSach.as_view()),
    path('api-chuong/<int:pk>', views.UpdateDeleteViewChuong.as_view()),
]

"""
urlpatterns = [
	path('api-overview', views.apiOverview, name="api-overview"),
	path('api-sach-list/', views.taskListSach, name="sach-list"),
	path('api-sach-detail/<str:pk>/', views.taskDetailSach, name="sach-detail"),
	path('api-sach-delete/<str:pk>/', views.taskDeleteSach, name="sach-delete"),
	path('api-chuong-list/', views.taskListChuong, name="sach-list"),
	path('api-chuong-detail/<str:pk>/', views.taskDetailChuong, name="sach-detail"),
	path('api-chuong-delete/<str:pk>/', views.taskDeleteChuong, name="sach-delete"),


]

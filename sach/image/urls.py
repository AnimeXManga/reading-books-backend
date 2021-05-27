from django.urls import path

from . import views

urlpatterns = [
	path('api-hinh', views.ListCreateViewHinh.as_view()),
]
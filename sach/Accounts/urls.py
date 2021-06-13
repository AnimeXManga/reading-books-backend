from django.urls import path

from . import views
app_name = 'accounts'
urlpatterns = [
	path('api-overview', views.apiOverview, name="api-overview"),
	path('api-account-list/', views.taskListAccount, name="account-list"),
	path('api-account-detail/<str:pk>/', views.taskDetailAccount, name="account-detail"),
    path('api-account-delete/<str:pk>/', views.taskDeleteAccount, name="account-delete"),

]
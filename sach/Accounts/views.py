from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AccountSerializer
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List-Profile-User':'/api-account-list/',
		'DetailView-Sach':'/api-account-detail/<str:pk>/',
		'Delete-Sach':'/api-account-delete/<str:pk>/',
		}
	return Response(api_urls)

@api_view(['GET'])
def taskListAccount(request):
	tasks = User.objects.all().order_by('id')
	serializer = AccountSerializer(tasks, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def taskDetailAccount(request, pk):
	tasks = User.objects.get(id=pk)
	serializer = AccountSerializer(tasks, many=False)

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDeleteAccount(request, pk):
	task = User.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')
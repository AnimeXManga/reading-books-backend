from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import AccountSerializer, ProfileSerializer
from .models import Profile


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
	tasks = Profile.objects.all().order_by('id')
	serializer = ProfileSerializer(tasks, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def taskDetailAccount(request, pk):
	tasks = Profile.objects.get(id=pk)
	serializer = ProfileSerializer(tasks, many=False)

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDeleteAccount(request, pk):
	task = Profile.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')
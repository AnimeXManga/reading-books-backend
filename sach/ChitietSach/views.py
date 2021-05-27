
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Sach, Chuong
from .serializer import SachSerializer, ChuongSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

# Create your views here.
"""
class ListCreateViewSach(ListCreateAPIView):
    model = Sach
    serializer_class = SachSerializer

    def get_queryset(self):
        return Sach.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = SachSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tao moi sach thanh cong!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Tao moi sach khong thanh cong!'
        }, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteViewSach(RetrieveUpdateDestroyAPIView):
    model = Sach
    serializer_class = SachSerializer

    def put(self, request, *args, **kwargs):
        sach = get_object_or_404(Sach, id=kwargs.get('pk'))
        serializer = SachSerializer(sach, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Cap nhat sach thanh cong!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Cap nhat sach khong thanh!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        sach = get_object_or_404(Sach, id=kwargs.get('pk'))
        sach.delete()

        return JsonResponse({
            'message': 'Delete Car successful!'
        }, status=status.HTTP_200_OK)

class ListCreateViewChuong(ListCreateAPIView):
    model = Chuong
    serializer_class = ChuongSerializer

    def get_queryset(self):
        return Chuong.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ChuongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Tao moi chuong thanh cong!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Tao moi chuong khong thanh cong!'
        }, status=status.HTTP_400_BAD_REQUEST)

class UpdateDeleteViewChuong(RetrieveUpdateDestroyAPIView):
    model = Chuong
    serializer_class = ChuongSerializer

    def put(self, request, *args, **kwargs):
        chuong = get_object_or_404(Sach, id=kwargs.get('pk'))
        serializer = ChuongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Cap nhat chuong thanh cong!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Cap nhat chuong khong thanh cong!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        chuong = get_object_or_404(Sach, id=kwargs.get('pk'))
        chuong.delete()

        return JsonResponse({
            'message': 'Xoa chuong thanh cong!'
        }, status=status.HTTP_200_OK)
"""
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List-Sach':'/api-sach-list/',
		'DetailView-Sach':'/api-sach-detail/<str:pk>/',
		'Delete-Sach':'/api-sach-delete/<str:pk>/',

		'List-Chuong': '/api-chuong-list/',
		'DetailView-Chuong': '/api-chuong-detail/<str:pk>/',
		'Delete-Chuong': '/api-chuong-delete/<str:pk>/',
		}
	return Response(api_urls)

@api_view(['GET'])
def taskListSach(request):
	tasks = Sach.objects.all().order_by('id')
	serializer = SachSerializer(tasks, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def taskDetailSach(request, pk):
	tasks = Sach.objects.get(id=pk)
	serializer = SachSerializer(tasks, many=False)

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDeleteSach(request, pk):
	task = Sach.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

@api_view(['GET'])
def taskListChuong(request):
	tasks = Chuong.objects.all().order_by('id')
	serializer = ChuongSerializer(tasks, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def taskDetailChuong(request, pk):
	tasks = Chuong.objects.get(id=pk)
	serializer = ChuongSerializer(tasks, many=False)

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDeleteChuong(request, pk):
	task = Chuong.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')




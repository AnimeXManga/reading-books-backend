from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render,  get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Sach, Chuong, Danhmuc, Theloai, Comment
from django.contrib.auth.models import User

from .serializer import SachSerializer, ChuongSerializer, DanhmucSerializer, TheloaiSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import CommentForm
from rest_framework import viewsets
import json


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List-Sach':'/api-sach-list/',
		'DetailView-Sach':'/api-sach-detail/<str:pk>/',
		'Delete-Sach':'/api-sach-delete/<str:pk>/',

		'List-Chuong': '/api-chuong-list/',
		'DetailView-Chuong': '/api-chuong-detail/<str:pk>/',
		'Delete-Chuong': '/api-chuong-delete/<str:pk>/',

		'List-DanhMuc': '/api-danhmuc-list/',
		'DetailView-DanhMuc': '/api-danhmuc-detail/<str:pk>/',
		'Delete-DanhMuc': '/api-danhmuc-delete/<str:pk>/',

        'List-Theloai': '/api-theloai-list/',
		'DetailView-Theloai': '/api-theloai-detail/<str:pk>/',
		'Delete-Theloai': '/api-theloai-delete/<str:pk>/',
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


@api_view(['GET'])
def taskListDanhmuc(request):
	tasks = Danhmuc.objects.all().order_by('id')
	serializer = DanhmucSerializer(tasks, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def taskDetailDanhmuc(request, pk):
	tasks = Danhmuc.objects.get(id=pk)
	serializer = DanhmucSerializer(tasks, many=False)

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDeleteDanhmuc(request, pk):
	task = Danhmuc.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')


@api_view(['GET'])
def taskListTheloai(request):
	tasks = Theloai.objects.all().order_by('id')
	serializer = TheloaiSerializer(tasks, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def taskDetailTheloai(request, pk):
	tasks = Theloai.objects.get(id=pk)
	serializer = TheloaiSerializer(tasks, many=False)

	return Response(serializer.data)

@api_view(['DELETE'])
def taskDeleteTheloai(request, pk):
	task = Theloai.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')


def post(request, pk):
    post = get_object_or_404(Chuong, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        body = request.body.decode('utf-8')
        jsonbody = json.loads(body)

        tasks = User.objects.get(id=jsonbody['author'])

        form = CommentForm(jsonbody, author=tasks, post=post)
        if form.is_valid():
            a = form.save()
            serializer = CommentSerializer(a, many=False)
            return JsonResponse({'status': 200, 'data': serializer.data, 'message': "Bình luận thành công"})

    return render(request, "post_detail.html/", {"post": post, "form": form})


class SachDanhmucViewset(viewsets.ModelViewSet):
    serializer_class = SachSerializer

    def get_queryset(self):
        sach_s = Sach.objects.all()
        return sach_s

    def retrieve(self, request, *args, **kwargs):
         params = kwargs
         print(params['pk'])
         params_list = params['pk'].split('-')
         sachs = Sach.objects.filter(
             danhmuc=params_list[0])
         serializer = SachSerializer(sachs, many=True)
         return Response(serializer.data)

class SachTheloaiViewset(viewsets.ModelViewSet):
    serializer_class = SachSerializer

    def get_queryset(self):
        sach_s = Sach.objects.all()
        return sach_s

    def retrieve(self, request, *args, **kwargs):
         params = kwargs
         print(params['pk'])
         params_list = params['pk'].split('-')
         sachs = Sach.objects.filter(
             theloai=params_list[0])
         serializer = SachSerializer(sachs, many=True)
         return Response(serializer.data)

class ChuongViewset(viewsets.ModelViewSet):
    serializer_class = ChuongSerializer

    def get_queryset(self):
        sach_s = Chuong.objects.all()
        return sach_s

    def retrieve(self, request, *args, **kwargs):
         params = kwargs
         print(params['pk'])
         params_list = params['pk'].split('-')
         sachs = Chuong.objects.filter(
             tieude=params_list[0])
         serializer = ChuongSerializer(sachs, many=True)
         return Response(serializer.data)

class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        sach_s = Comment.objects.all()
        return sach_s

    def retrieve(self, request, *args, **kwargs):
         params = kwargs
         print(params['pk'])
         params_list = params['pk'].split('-')
         sachs = Comment.objects.filter(
             post=params_list[0]).order_by('-date')

         serializer = CommentSerializer(sachs, many=True)
         # return JsonResponse(serializer.data, safe = False)
         return  Response(serializer.data)
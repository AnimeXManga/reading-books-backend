from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import render,  get_object_or_404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Sach, Chuong, Danhmuc, Theloai, Comment
from .serializer import SachSerializer, ChuongSerializer, DanhmucSerializer, TheloaiSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import CommentForm
from rest_framework import viewsets


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

def post_detail(request, pk):
    template_name = 'post_detail.html'
    post = get_object_or_404(Chuong, pk=pk)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request,"post_detail.html", {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


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
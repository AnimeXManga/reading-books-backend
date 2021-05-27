from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from .serializer import HinhSerializer
from .models import Hinh
# Create your views here.

class ListCreateViewHinh(ListCreateAPIView):
    model = Hinh
    serializer_class = HinhSerializer

    def get_queryset(self):
        return Hinh.objects.all()

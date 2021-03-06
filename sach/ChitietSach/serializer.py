from rest_framework import serializers
from django.db.models import fields
from .models import Sach, Chuong, Danhmuc, Theloai, Comment

class SachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sach
        fields = ('id','tieude','hinh','tacgia','danhmuc','theloai','mota')


class ChuongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chuong
        fields = ('id','sochuong','noidung','tieude')


class DanhmucSerializer(serializers.ModelSerializer):
    class Meta:
        model = Danhmuc
        fields = ('id', 'danhmuc')

class TheloaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theloai
        fields = ('id', 'thloai')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post','author','body','date')
from rest_framework import serializers

from .models import Sach, Chuong

class SachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sach
        fields = ('id','tieude','hinh','tacgia','danhmuc','theloai','mota')


class ChuongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chuong
        fields = ('id','sochuong','noidung','tieude')

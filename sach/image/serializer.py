from rest_framework import serializers

from .models import Hinh

class HinhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hinh
        fields = ('id','hinh')
from django.contrib.auth.models import User
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')
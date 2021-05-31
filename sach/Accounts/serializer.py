from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','avatar','bio')
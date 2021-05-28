from django.shortcuts import render
from .forms import DangkyForm, DangnhapForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import json


class DangkyThanhvien(View):
    def get(self, request):
        rF = DangkyForm
        return render(request, 'UserMembers/dangky.html', {'rF': rF})

    def post(self, request):
        body = request.body.decode('utf-8')
        jsonbody = json.loads(body)

        username = jsonbody['username']
        email = jsonbody['email']
        password = jsonbody['password']

        print(username, email, password)


        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return Response('Create user success')


class DangnhapThanhvien(View):
    def get(self, request):
        lF = DangnhapForm
        return render(request, 'UserMembers/dangnhap.html', {'lF': lF})

    def post(self, request):
        body = request.body.decode('utf-8')
        jsonbody = json.loads(body)

        username = jsonbody['username']
        password = jsonbody['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('Login user success')
        else:
            return HttpResponse('Login user fail')

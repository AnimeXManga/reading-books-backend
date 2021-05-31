from django.shortcuts import render
from .forms import DangkyForm, DangnhapForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json


class DangkyThanhvien(View):
    def get(self, request):
        rF = DangkyForm
        return render(request, 'UserMembers/dangky.html', {'rF': rF})

    def post(self, request):
        body = request.body.decode('utf-8')
        jsonbody = json.loads(body)

        print(jsonbody)

        username = jsonbody['username']
        email = jsonbody['email']
        password = jsonbody['password']


        user = User.objects.create_user(username, email, password)
        user.save()
        return JsonResponse({'message': "Dang ky thanh cong", 'status': 200})
        # return HttpResponse('Login user success')


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
            return JsonResponse({'message': "Đăng nhập thành công", 'status': 200})
        else:
            return JsonResponse({'message': "Đăng nhập không thành công", 'status': 200})

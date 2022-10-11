from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializers
from django.views import View
from django.contrib.auth import authenticate, login


class index(View):
    def get(self,request):
        return render("index.html")


class Register(View):
    def post(self, request):
        user_obj = request.data
        user = User.objects.create_user(username=user_obj.username,
                                        password=user_obj.password,
                                        phone=user_obj.phone,
                                        email=user_obj.email)
        return redirect("login.html")


class Login(View):
    def post(self, request):
        username = request.POST.get("user")
        passwd = request.POST.get("passwd")
        if User.objects.authenticate(username=username, password=passwd):
            return redirect("index.html")




from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
# Create your views here.

from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib.auth.decorators import login_required


# # 主页

class Index(View):
    # @login_required()
    def get(self, request):
        return render(request, "index.html")


# 用户退出
class Quit(View):
    def get(self, request):
        logout(request)
        return redirect("/")


# 注册
class Register(View):
    def get(self, request):
        return render(request, "register.html")

    def post(self, request):
        user_obj = request.POST.get
        try:
            if User.objects.get(username=user_obj('username')):
                return render(request, "register.html", {'msg_t': True})
        except:
            if user_obj("password") == user_obj("repasswd"):
                user = User.objects.create_user(username=user_obj("username"),
                                                password=user_obj("password"),
                                                phone=user_obj("phone"),
                                                email=user_obj("email"))
                user.save()
            else:
                return render(request, "register.html", {'msg': True})

            return redirect("/login/")


# 登录
class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        username = request.POST.get("user")
        passwd = request.POST.get("passwd")
        user = authenticate(request, username=username, password=passwd)
        if user is not None:
            login(request, user)
        else:
            return render(request, "login.html", {'message': True})

        return render(request, 'index.html', {"user": username,"msg": True})


class Edit(View):
    def get(self, request):
        return render(request, "edit.html")

    def post(self, request):
        user_obj = request.POST.get
        username = user_obj('username')
        phone = user_obj('phone')
        email = user_obj('email')
        passwd = user_obj('password')
        try:
            if User.objects.get(username=username, phone=phone, email=email):
                if passwd == user_obj('repasswd'):
                    user = User.objects.get(username=username)
                    user.set_password(passwd)
                    user.save()
                    return redirect("/login/")
                else:
                    return render(request, "edit.html", {"msg_p": True})
        except:
            return render(request, "edit.html", {"msg": True})

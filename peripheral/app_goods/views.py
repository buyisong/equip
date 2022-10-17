from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from app_goods.models import *
from django.views import View

# 分页
from django.core.paginator import Paginator
import json
from django.http import JsonResponse


# Create your views here.
class Mouse(View):

    def get(self, request):
        goods_spu = GoodsSpu.objects.filter(type=1)
        print(goods_spu)
        print(goods_spu[0].sp_picture.name)
        return render(request, "mouse.html", locals())

    def post(self, request):
        pass


class Headsets(View):

    def get(self, request):
        return render(request, "headsets.html", locals())

    def post(self, request):
        pass


class Keyboard(View):

    def get(self, request):
        type_1 = GoodsType.objects.all()
        paginator = Paginator(type_1, 3)
        try:
            print(type_1)
            page_data = request.GET.get('page')
            print(page_data)
            print(type(page_data))
            print(333333333333333)
            # 每页显示三条数据
            print(222222222222222222222)
            posts = Paginator()
            posts.page(page_data)
            # print(444444444444444444)
        except  Exception:
            print(1111111111111111111111)

            # posts = Paginator.page(1)
            return render(request, "keyboard.html", locals())

        return render(request, "keyboard.html", locals())

    def post(request):
        pass

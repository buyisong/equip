from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User

u = User.objects.get(username='')

# set_password函数,设置密码;
u.set_password('123456')

# check_password函数,检查密码;
u.check_password('123456')
True

# save函数,保存密码;
u.save()























































# 改密码
# from django.contrib.auth.models import User
#
# u = User.objects.get(username='gsj666')
#
# # set_password函数,设置密码;
# u.set_password('99955665335')
#
# # check_password函数,检查密码;
# u.check_password('123456')
# True
#
# # save函数,保存密码;
# u.save()
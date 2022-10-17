from django.urls import path, re_path
from app_goods.views import *

urlpatterns = [
    path('headsets/', Headsets.as_view()),
    path('keyboard/', Keyboard.as_view()),
    path('mouse/', Mouse.as_view()),

]

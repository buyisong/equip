from django.urls import path, re_path
from app_login.views import *


urlpatterns = [
    path('login/', Login.as_view()),
    path('register/', Register.as_view()),
    path('', Index.as_view(), name='index'),
    path('logout/', Quit.as_view()),
    path('edit/', Edit.as_view())
]

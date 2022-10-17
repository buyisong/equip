from django.db import models

__all__ = ['User']

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=11)

# def __str__(self):
#     return self.username

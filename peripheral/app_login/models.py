from django.db import models


# Create your models here.

from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    phone = models.CharField(max_length=11, null=True, unique=True)




def __str__(self):
    return self.username








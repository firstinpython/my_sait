from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Users(AbstractUser):
    avatar = models.FileField(verbose_name="avatar", upload_to="avatar")
    age = models.PositiveIntegerField(verbose_name="age")

    def __str__(self):
        return f"{self.username} {self.age}"

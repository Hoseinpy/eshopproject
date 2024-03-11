from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=20)
    email_verify_code = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='files/user_avatars', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username



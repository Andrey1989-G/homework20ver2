from django.db import models
from django.contrib.auth.models import AbstractUser
from secrets import token_hex
from for_hw192.models import NULLABLE
# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна', **NULLABLE)
    verify_token = models.CharField(default=token_hex(6))
    is_active = models.BooleanField(default=False, verbose_name='активен')
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

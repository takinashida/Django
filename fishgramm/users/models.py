from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    username = None
    email = models.CharField(unique=True, verbose_name="Email")
    avatar = models.ImageField(upload_to='contents/image/', blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name="Номер телефона", blank=True, null=True)
    country = models.CharField(max_length = 100, verbose_name="Страна проживания", blank=True, null=True)
    token = models.CharField(max_length = 100, verbose_name="Токен активации", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
        ordering=["email"]

    def __str__(self):
        return self.email

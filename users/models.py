from django.contrib.auth.models import AbstractUser
from django.db import models
from config import settings


class User(AbstractUser):
    """Model definition for User."""

    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, verbose_name="телефон", **settings.NULLABLE)
    city = models.CharField(max_length=35, verbose_name="город", **settings.NULLABLE)
    avatar = models.ImageField(
        upload_to="users/avatars", verbose_name="аватар", **settings.NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

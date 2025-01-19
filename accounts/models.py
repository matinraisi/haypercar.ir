# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)

    # اضافه کردن related_name به user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # اینجا تغییر داده می‌شود
        blank=True,
    )

    def __str__(self):
        return self.username

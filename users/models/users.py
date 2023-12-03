from django.contrib.auth.models import AbstractUser
from django.db import models

from users.models.managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Email', unique=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

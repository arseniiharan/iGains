from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.managers import CustomUserManager
from users.models.profile import Profile


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
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


# Created a signal function for safe profile creation
@receiver(post_save, sender=User)
def post_save_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

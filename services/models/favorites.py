from django.contrib.auth import get_user_model
from django.db import models
from services.models.musclemap import Exercises

User = get_user_model()


# Creating 'Favorites' table, so the user can choose his favorite exercise from musclemap table exercises
class Favorites(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_id'
    )
    exercise = models.ForeignKey(
        Exercises, on_delete=models.CASCADE, related_name='exercise_id', verbose_name='Favorite Exercises',
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"

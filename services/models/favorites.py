from django.contrib.auth import get_user_model
from django.db import models
from services.models.musclemap import Chest, Abs, Back, Arms, Shoulders, Legs

User = get_user_model()


# Creating 'Favorites' table, so the user can choose his favorite exercise from every muscle table exercises
class Favorites(models.Model):
    user = models.ForeignKey(
        User, models.CASCADE, related_name='users_exercises'
    )
    chest_exercises = models.ForeignKey(
        Chest, models.CASCADE, related_name='chest_favorites', verbose_name='Chest Favorites',
        blank=True, null=True
    )
    abs_exercises = models.ForeignKey(
        Abs, models.CASCADE, related_name='abs_favorites', verbose_name='Abs Favorites',
        blank=True, null=True
    )
    back_exercises = models.ForeignKey(
        Back, models.CASCADE, related_name='back_favorites', verbose_name='Back Favorites',
        blank=True, null=True
    )
    arms_exercises = models.ForeignKey(
        Arms, models.CASCADE, related_name='arms_favorites', verbose_name='Arms Favorites',
        blank=True, null=True
    )
    shoulders_exercises = models.ForeignKey(
        Shoulders, models.CASCADE, related_name='shoulders_favorites', verbose_name='Shoulders Favorites',
        blank=True, null=True
    )
    legs_exercises = models.ForeignKey(
        Legs, models.CASCADE, related_name='legs_favorites', verbose_name='Legs Favorites',
        blank=True, null=True
    )

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"

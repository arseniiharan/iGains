from django.contrib.auth import get_user_model
from django.db import models
from services.models.musclemap import Exercises

User = get_user_model()


class LatestTraining(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_id_training'
    )
    exercise = models.ForeignKey(
        Exercises, on_delete=models.CASCADE, related_name='exercise_id_training', verbose_name='Latest Training',
        blank=True, null=True
    )
    training_date = models.CharField(verbose_name='Date', blank=True, null=True)
    training_time = models.IntegerField(verbose_name='Time', blank=True, null=True)

    class Meta:
        verbose_name = "Training"
        verbose_name_plural = "Trainings"

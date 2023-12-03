from django.contrib.auth import get_user_model
from django.db import models


# Creating profiles for users to contain additional information required in app
class Profile(models.Model):
    GENDER_CHOICES = [  # Creating a tuple to restrict users possibility choice in options
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField('users.User', models.CASCADE, related_name='profile', verbose_name='user', primary_key=True)
    age = models.SmallIntegerField(verbose_name='age')
    gender = models.CharField(verbose_name='gender', choices=GENDER_CHOICES, max_length=1)
    weight = models.SmallIntegerField(verbose_name='weight')
    height = models.SmallIntegerField(verbose_name='height')
    experience = models.BooleanField(verbose_name='experience', default=False)
    photo = models.ImageField(verbose_name='photo')

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'

    def __str__(self):
        return f'{self.user} ({self.pk})'


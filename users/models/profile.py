from django.contrib.auth import get_user_model
from django.db import models


# Creating profiles for users to contain additional information required in app
class Profile(models.Model):
    GENDER_CHOICES = [  # Creating a tuple to restrict users possibility choice in options
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField('users.User', models.CASCADE, related_name='profile', verbose_name='user',
                                primary_key=True)
    age = models.SmallIntegerField(verbose_name='age', null=True, blank=True)
    gender = models.CharField(verbose_name='gender', choices=GENDER_CHOICES, max_length=1, null=True, blank=True)
    weight = models.SmallIntegerField(verbose_name='weight', null=True, blank=True)
    height = models.SmallIntegerField(verbose_name='height', null=True, blank=True)
    experience = models.BooleanField(verbose_name='experience', default=False, null=True, blank=True)
    photo = models.ImageField(verbose_name='photo', null=True, blank=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profiles'

    def __str__(self):
        return f'{self.user} ({self.pk})'


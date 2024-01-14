from django.db import models


# Creating a database to contain same exercises for all users
class Exercises(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Middle', 'Middle'),
        ('Advanced', 'Advanced'),
    ]

    CATEGORY_CHOICES = [
        ('Yoga', 'Yoga'),
        ('Gym', 'Gym'),
        ('Running', 'Running'),
        ('Stretching', 'Stretching'),
    ]

    exercise_level = models.CharField(verbose_name='Level', choices=LEVEL_CHOICES, max_length=255)
    exercise_category = models.CharField(verbose_name='Category', choices=CATEGORY_CHOICES, max_length=255)
    exercise_image = models.URLField()
    exercise_title = models.CharField(verbose_name='Title', max_length=255)
    exercise_desc = models.CharField(verbose_name='Description', max_length=500)
    exercise_duration = models.PositiveIntegerField(verbose_name='Duration', null=True, blank=True)
    exercise_kcal = models.PositiveIntegerField(verbose_name='Calories', null=True, blank=True)

    def __str__(self):
        return f'{self.exercise_title}'

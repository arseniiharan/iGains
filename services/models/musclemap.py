from django.db import models


# Creating a parent class for separating every muscle table
class Musclemap(models.Model):
    exercise_image = models.URLField()
    exercise_title = models.CharField(verbose_name='Title', max_length=255)
    exercise_desc = models.CharField(verbose_name='Description', max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.exercise_title}'


# Creating child classes lower
class Chest(Musclemap):
    pass

    class Meta:
        verbose_name = "Chest"
        verbose_name_plural = "Chest exercises"


class Abs(Musclemap):
    pass

    class Meta:
        verbose_name = "Abs"
        verbose_name_plural = "Abs exercises"


class Back(Musclemap):
    pass

    class Meta:
        verbose_name = "Back"
        verbose_name_plural = "Back exercises"


class Arms(Musclemap):
    pass

    class Meta:
        verbose_name = "Arms"
        verbose_name_plural = "Arms exercises"


class Shoulders(Musclemap):
    pass

    class Meta:
        verbose_name = "Shoulders"
        verbose_name_plural = "Shoulders exercises"


class Legs(Musclemap):
    pass

    class Meta:
        verbose_name = "Legs"
        verbose_name_plural = "Legs exercises"

from django.contrib import admin

from services.models.favorites import Favorites
from services.models.musclemap import Exercises
from services.models.trainings import LatestTraining


#########################################################
# INLINES
#########################################################

#########################################################
# MODELS
#########################################################
@admin.register(Exercises)
class ExercisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise_level', 'exercise_category', 'exercise_image', 'exercise_title', 'exercise_desc')


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'exercise_id')


@admin.register(LatestTraining)
class TrainingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'exercise_id', 'training_date', 'training_time')

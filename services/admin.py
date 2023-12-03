from django.contrib import admin

from services.models.favorites import Favorites
from services.models.musclemap import Chest, Abs, Back, Arms, Shoulders, Legs


#########################################################
# INLINES
#########################################################

#########################################################
# MODELS
#########################################################
@admin.register(Chest)
class ChestAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise_image', 'exercise_title', 'exercise_desc')


@admin.register(Abs)
class AbsAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise_image', 'exercise_title', 'exercise_desc')


@admin.register(Back)
class BackAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise_image', 'exercise_title', 'exercise_desc')


@admin.register(Arms)
class ArmsAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise_image', 'exercise_title', 'exercise_desc')


@admin.register(Shoulders)
class ShouldersAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise_image', 'exercise_title', 'exercise_desc')


@admin.register(Legs)
class LegsAdmin(admin.ModelAdmin):
    list_display = ('id', 'exercise_image', 'exercise_title', 'exercise_desc')


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    pass

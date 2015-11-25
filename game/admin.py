from django.contrib import admin
from game.models import *

class GameAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', )

class GameImagesAdmin(admin.ModelAdmin):
    list_display = ('code', 'img', )

admin.site.register(Games, GameAdmin)
admin.site.register(GameImages, GameImagesAdmin)
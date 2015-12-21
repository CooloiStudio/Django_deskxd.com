from django.contrib import admin
from game.models import *

class GameInfoInline(admin.StackedInline):
    model = GameInfo
    extra = 3

class GameAdmin(admin.ModelAdmin):
    list_display = ('code', 'url', )
    inlines = [GameInfoInline]

class GameImagesAdmin(admin.ModelAdmin):
    list_display = ('code', 'img', )

admin.site.register(Games, GameAdmin)
admin.site.register(GameImages, GameImagesAdmin)
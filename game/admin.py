from django.contrib import admin
from game.models import *

class GameInfoInline(admin.StackedInline):
    model = GameInfo
    extra = 3

class GameAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'url', )
    inlines = [GameInfoInline]

class GameImagesAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'img', )


class GSectionInline(admin.StackedInline):
    model = GSectionInfo
    extra = 3


class GSectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'basepage', )
    inlines = [GSectionInline]


class GBasePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'remark', )


admin.site.register(GBasePage, GBasePageAdmin)
admin.site.register(Games, GameAdmin)
admin.site.register(GameImages, GameImagesAdmin)
admin.site.register(GSection, GSectionAdmin)
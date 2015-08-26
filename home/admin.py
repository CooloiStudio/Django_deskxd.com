from django.contrib import admin
from . import models


class IntroduceImageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'url', )

class GroupInfoAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'info_class', )

class GroupAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', )


admin.site.register(models.IntroduceImage, IntroduceImageAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.GroupInfo, GroupInfoAdmin)
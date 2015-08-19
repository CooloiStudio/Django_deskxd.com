from django.contrib import admin
from . import models

class BaseHtmlAdmin(admin.ModelAdmin):
    list_display = ('name', )

class SiteAdmin(admin.ModelAdmin):
    list_display = ('code', 'class_name', 'id_name', 'default', )

class SiteTitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'default', )

class IntroduceImageAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'url', )

class GroupInfoAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'info_class', )

class GroupAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'group_class', )

class PoweredByAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', )

class MenuAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', )

admin.site.register(models.BaseHtml, BaseHtmlAdmin)
admin.site.register(models.Site, SiteAdmin)
admin.site.register(models.SiteTitle, SiteTitleAdmin)
admin.site.register(models.IntroduceImage, IntroduceImageAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.GroupInfo, GroupInfoAdmin)
admin.site.register(models.PoweredBy, PoweredByAdmin)
admin.site.register(models.Menu, MenuAdmin)
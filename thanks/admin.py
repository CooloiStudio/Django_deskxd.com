from django.contrib import admin
from thanks.models import *

class ThanksAdmin(admin.ModelAdmin):
    list_display = ('name', )


class TSectionInline(admin.StackedInline):
    model = TSectionInfo
    extra = 3


class TSectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'basepage', )
    inlines = [TSectionInline]


admin.site.register(Thanks, ThanksAdmin)
admin.site.register(TSection, TSectionAdmin)
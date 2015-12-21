from django.contrib import admin
from information.models import *


class InfoInline(admin.StackedInline):
    model = InformationInfo
    extra = 3


class InformationAdmin(admin.ModelAdmin):
    list_display = ('code', 'img', )
    inlines = [InfoInline]


admin.site.register(Information, InformationAdmin)

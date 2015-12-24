from django.contrib import admin
from information.models import *


class InfoInline(admin.StackedInline):
    model = InformationInfo
    extra = 3


class InformationAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'img', )
    inlines = [InfoInline]


class ProtocolInline(admin.StackedInline):
    model = ProtocolInfo
    extra = 3


class ProtocolAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'url', )
    inlines = [ProtocolInline]


class InfoSectionInline(admin.StackedInline):
    model = InfoSectionInfo
    extra = 3


class InfoSectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'basepage', )
    inlines = [InfoSectionInline]


admin.site.register(Information, InformationAdmin)
admin.site.register(Protocol, ProtocolAdmin)
admin.site.register(InfoSection, InfoSectionAdmin)

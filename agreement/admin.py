from django.contrib import admin
from agreement.models import *

class AgreementAdmin(admin.ModelAdmin):
    list_display = ("title", "language", )

class PrivacyAdmin(admin.ModelAdmin):
    list_display = ("title", "language", )


class ASectionInline(admin.StackedInline):
    model = ASectionInfo
    extra = 3


class ASectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'basepage', )
    inlines = [ASectionInline]


class PSectionInline(admin.StackedInline):
    model = PSectionInfo
    extra = 3


class PSectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'basepage', )
    inlines = [PSectionInline]


class ABasePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'remark', )


admin.site.register(ABasePage, ABasePageAdmin)
admin.site.register(Agreement, AgreementAdmin)
admin.site.register(Privacy, PrivacyAdmin)
admin.site.register(ASection, ASectionAdmin)
admin.site.register(PSection, PSectionAdmin)
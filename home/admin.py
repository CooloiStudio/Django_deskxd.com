from django.contrib import admin
from home.models import *

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', )


class IntroduceInfoInline(admin.StackedInline):
    model = IntroduceInfo
    extra = 3


class IntroduceImageAdmin(admin.ModelAdmin):
    list_display = ('code', 'url', )
    inlines = [IntroduceInfoInline]


class MenuInfoInline(admin.StackedInline):
    model = MenuInfo
    extra = 3


class MenuAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'url', )
    inlines = [MenuInfoInline]


class ContactInline(admin.StackedInline):
    model = ContactInfo
    extra = 3


class ContactAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'remark', )
    inlines = [ContactInline]


class SectionInline(admin.StackedInline):
    model = SectionInfo
    extra = 3


class SectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'basepage', )
    inlines = [SectionInline]



admin.site.register(Languages, LanguageAdmin)
admin.site.register(IntroduceImage, IntroduceImageAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Contact, ContactAdmin)
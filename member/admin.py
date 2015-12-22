from django.contrib import admin
from member.models import *


class MemberInline(admin.StackedInline):
    model = MemberInfo
    extra = 3


class MemberAdmin(admin.ModelAdmin):
    list_display = ('code', 'url', )
    inlines = [MemberInline]


class MSectionInline(admin.StackedInline):
    model = MSectionInfo
    extra = 3


class MSectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'basepage', )
    inlines = [MSectionInline]


admin.site.register(Member, MemberAdmin)
admin.site.register(MSection, MSectionAdmin)

from django.contrib import admin
from member.models import *


class MemberInline(admin.StackedInline):
    model = MemberInfo
    extra = 3


class MemberAdmin(admin.ModelAdmin):
    list_display = ('code', 'url', )
    inlines = [MemberInline]


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


class MSectionInline(admin.StackedInline):
    model = MSectionInfo
    extra = 3


class MSectionAdmin(admin.ModelAdmin):
    list_display = ('code', 'sort', 'basepage', )
    inlines = [MSectionInline]


class MBasePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'remark', )


admin.site.register(MBasePage, MBasePageAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(MSection, MSectionAdmin)
admin.site.register(Group, GroupAdmin)

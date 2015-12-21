from django.contrib import admin
from member.models import *

class MemberAdmin(admin.ModelAdmin):
    list_display = ('code', 'url', )

admin.site.register(Member, MemberAdmin)

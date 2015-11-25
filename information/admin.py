from django.contrib import admin
from information.models import *

class InformationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', )

admin.site.register(Information, InformationAdmin)

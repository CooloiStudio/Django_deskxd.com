from django.contrib import admin
from thanks.models import *

class ThanksAdmin(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(Thanks, ThanksAdmin)
from django.contrib import admin
from home.models import *

class IntroduceImageAdmin(admin.ModelAdmin):
    list_display = ('code', 'url', )


admin.site.register(IntroduceImage, IntroduceImageAdmin)
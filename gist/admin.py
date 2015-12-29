from django.contrib import admin
from gist.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)



from django.contrib import admin
from .models import *


class LineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'number', 'color')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'number',)


admin.site.register(Line, LineAdmin)

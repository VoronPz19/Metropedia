from django.contrib import admin
from .models import *


class LineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'number', 'color')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'number',)


class CityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


admin.site.register(Line, LineAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(LineInfo)
admin.site.register(CityInfo)

from django.contrib import admin
from .models import *


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'time_created', 'image')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)

admin.site.register(Blog, BlogAdmin)

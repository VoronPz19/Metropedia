from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'time_created', 'image')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)


admin.site.register(Blog, BlogAdmin)

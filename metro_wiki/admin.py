from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class DepotAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Depot
        fields = '__all__'


class TrainAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Train
        fields = '__all__'


class StationAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Station
        fields = '__all__'


class LineAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Line
        fields = '__all__'


class CityAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = City
        fields = '__all__'


class DepotAdmin(admin.ModelAdmin):
    form = DepotAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'city', )
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


class TrainAdmin(admin.ModelAdmin):
    form = TrainAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


class StationAdmin(admin.ModelAdmin):
    form = StationAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'index', 'status', 'line')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'line',)
    filter_horizontal = ('transfer',)


class LineAdmin(admin.ModelAdmin):
    form = LineAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'number', 'color')
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'number',)


class CityAdmin(admin.ModelAdmin):
    form = CityAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)


admin.site.register(Depot, DepotAdmin)
admin.site.register(Train, TrainAdmin)
admin.site.register(Station, StationAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(City, CityAdmin)

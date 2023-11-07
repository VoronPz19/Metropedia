from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple, RadioSelect
from .models import *


class AddCityForm(ModelForm):
    class Meta:
        model = City
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False


class AddLineForm(ModelForm):
    class Meta:
        model = Line
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False


class AddStationForm(ModelForm):
    class Meta:
        model = Station
        fields = '__all__'
        widgets = {
            'transfer': CheckboxSelectMultiple(),
            'line': RadioSelect(),
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False


class AddTrainForm(ModelForm):
    class Meta:
        model = Line
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False


class AddDepotForm(ModelForm):
    class Meta:
        model = Depot
        fields = '__all__'
        widgets = {
            'trains': CheckboxSelectMultiple(),
            'lines': CheckboxSelectMultiple(),
            'city': RadioSelect(),
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False

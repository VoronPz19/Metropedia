from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple, RadioSelect
from .models import *


class AddCityForm(ModelForm):
    image = forms.ImageField(label='Картинка', widget=forms.FileInput(attrs={'class': 'file-input'}))

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
            field.widget.attrs.update({'class': 'form-input', 'autocomplete': 'off'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False
        self.fields['slug'].widget.attrs.update(
            {'placeholder': 'Оставьте поле пустым, чтобы сгенерировать автоматически'})
        self.fields['image'].required = False


class AddLineForm(ModelForm):
    image = forms.ImageField(label='Картинка', widget=forms.FileInput(attrs={'class': 'file-input'}))

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
            field.widget.attrs.update({'class': 'form-input', 'autocomplete': 'off'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False
        self.fields['slug'].widget.attrs.update(
            {'placeholder': 'Оставьте поле пустым, чтобы сгенерировать автоматически'})
        self.fields['image'].required = False


class AddStationForm(ModelForm):
    image = forms.ImageField(label='Картинка', widget=forms.FileInput(attrs={'class': 'file-input'}))

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
            field.widget.attrs.update({'class': 'form-input', 'autocomplete': 'off'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False
        self.fields['slug'].widget.attrs.update(
            {'placeholder': 'Оставьте поле пустым, чтобы сгенерировать автоматически'})
        self.fields['image'].required = False


class OrderingStationForm(forms.Form):
    ordering = forms.ChoiceField(label='Сортировка', required=False, choices=[
        ['title', 'По алфавиту (По возрастанию)'], ['-title', 'По алфавиту (По убиванию)'],
        ['line', 'По номеру линий (По возрастанию)'], ['-line', 'По номеру линий (По убиванию)'],
        ['index', 'По индексаций (С севера/востока на юг/запад)'],
        ['-index', 'По индексаций (С юга/запада на север/восток)']
    ])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input', 'autocomplete': 'off'})


class AddTrainForm(ModelForm):
    image = forms.ImageField(label='Картинка', widget=forms.FileInput(attrs={'class': 'file-input'}))

    class Meta:
        model = Train
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'slug': forms.TextInput(),
            'content': forms.TextInput(attrs={'cols': 60, 'rows': 10}),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-input', 'autocomplete': 'off'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False
        self.fields['slug'].widget.attrs.update(
            {'placeholder': 'Оставьте поле пустым, чтобы сгенерировать автоматически'})
        self.fields['image'].required = False


class AddDepotForm(ModelForm):
    image = forms.ImageField(label='Картинка', widget=forms.FileInput(attrs={'class': 'file-input'}))
    
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
            field.widget.attrs.update({'class': 'form-input', 'autocomplete': 'off'})

        self.fields['content'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
        self.fields['content'].required = False
        self.fields['slug'].widget.attrs.update(
            {'placeholder': 'Оставьте поле пустым, чтобы сгенерировать автоматически'})
        self.fields['image'].required = False

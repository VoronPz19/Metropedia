from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import *


class AddPostForm(ModelForm):
    image = forms.ImageField(label='Картинка', widget=forms.FileInput(attrs={'class': 'file-input'}))

    class Meta:
        model = Blog
        exclude = ['time_created', 'time_update', 'is_public', 'owner']
        widgets = {
            'line': CheckboxSelectMultiple(),
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
        self.fields['slug'].required = False
        self.fields['image'].required = False

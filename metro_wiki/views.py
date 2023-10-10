from django.views.generic import ListView, DetailView
from .models import *
from main_page.utils import DataMixin


class Cities(DataMixin, ListView):
    model = City
    template_name = 'wiki/cities/index.html'
    context_object_name = 'cities_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Города')
        return dict(list(context.items()) + list(c_def.items()))


class ShowCity(DataMixin, DetailView):
    model = City
    template_name = 'wiki/cities/city.html'
    slug_url_kwarg = 'cities_slug'
    context_object_name = 'cities'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['cities'])
        return dict(list(context.items()) + list(c_def.items()))

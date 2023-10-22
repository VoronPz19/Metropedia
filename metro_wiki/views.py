from django.views.generic import DetailView
from .models import *
from main_page.utils import DataMixin


class ShowCity(DataMixin, DetailView):
    model = City
    template_name = 'wiki/city.html'
    slug_url_kwarg = 'cities_slug'
    context_object_name = 'cities'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['cities'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowLine(DataMixin, DetailView):
    model = Line
    template_name = 'wiki/line.html'
    slug_url_kwarg = 'line_slug'
    context_object_name = 'line'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['line'])
        return dict(list(context.items()) + list(c_def.items()))

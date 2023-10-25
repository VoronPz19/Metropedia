from django.views.generic import ListView, DetailView
from .models import *
from main_page.utils import DataMixin


class Cities(DataMixin, ListView):
    model = City
    template_name = 'wiki/categories/cities.html'
    context_object_name = 'cities'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Города')
        return dict(list(context.items()) + list(c_def.items()))


class Lines(DataMixin, ListView):
    model = Line
    template_name = 'wiki/categories/lines.html'
    context_object_name = 'lines'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Линий')
        return dict(list(context.items()) + list(c_def.items()))


class Stations(DataMixin, ListView):
    model = Station
    template_name = 'wiki/categories/stations.html'
    context_object_name = 'stations'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Станций')
        return dict(list(context.items()) + list(c_def.items()))


class ShowCity(DataMixin, DetailView):
    model = City
    template_name = 'wiki/city.html'
    slug_url_kwarg = 'city_slug'
    context_object_name = 'city'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['city'])
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


class ShowStation(DataMixin, DetailView):
    model = Station
    template_name = 'wiki/station.html'
    slug_url_kwarg = 'station_slug'
    context_object_name = 'station'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['station'])
        return dict(list(context.items()) + list(c_def.items()))

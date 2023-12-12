from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import *
from metro_blog.models import Blog

from main_page.utils import DataMixin


# -- Categories --


class Cities(DataMixin, ListView):
    model = City
    template_name = 'wiki/categories/cities.html'
    context_object_name = 'cities'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Города')
        return dict(list(context.items()) + list(c_def.items()))


class Lines(DataMixin, ListView):
    model = Line
    template_name = 'wiki/categories/lines.html'
    context_object_name = 'lines'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all
        context['lines'] = Line.objects.extra(select={'sorted_num': 'CAST(number AS INTEGER)'}) \
            .order_by('sorted_num')
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Линий')
        return dict(list(context.items()) + list(c_def.items()))


class Stations(DataMixin, ListView):
    model = Station
    template_name = 'wiki/categories/stations.html'
    context_object_name = 'stations'
    sort_form = OrderingStationForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all
        context['stations'] = Station.objects.order_by('line', 'title')
        context['ordering'] = OrderingStationForm()
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Станций')
        return dict(list(context.items()) + list(c_def.items()))


class Trains(DataMixin, ListView):
    model = Train
    template_name = 'wiki/categories/trains.html'
    context_object_name = 'trains'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Поезда')
        return dict(list(context.items()) + list(c_def.items()))


class Depots(DataMixin, ListView):
    model = Depot
    template_name = 'wiki/categories/depots.html'
    context_object_name = 'depots'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Депо')
        return dict(list(context.items()) + list(c_def.items()))


# -- Objects --


class ShowCity(DataMixin, DetailView):
    model = City
    template_name = 'wiki/objects/city.html'
    slug_url_kwarg = 'city_slug'
    context_object_name = 'city'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lines'] = Line.objects.extra(select={'sorted_num': 'CAST(number AS INTEGER)'}) \
            .order_by('sorted_num')
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=context['city'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowLine(DataMixin, DetailView):
    model = Line
    template_name = 'wiki/objects/line.html'
    slug_url_kwarg = 'line_slug'
    context_object_name = 'line'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['depot'] = Depot.objects.all()
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=context['line'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowStation(DataMixin, DetailView):
    model = Station
    template_name = 'wiki/objects/station.html'
    slug_url_kwarg = 'station_slug'
    context_object_name = 'station'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        context['depot'] = Depot.objects.all()
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=context['station'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowTrain(DataMixin, DetailView):
    model = Train
    template_name = 'wiki/objects/train.html'
    slug_url_kwarg = 'train_slug'
    context_object_name = 'train'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title=context['train'])
        return dict(list(context.items()) + list(c_def.items()))


class ShowDepot(DataMixin, DetailView):
    model = Depot
    template_name = 'wiki/objects/depot.html'
    slug_url_kwarg = 'depot_slug'
    context_object_name = 'depot'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['station_list'] = Station.objects.all()
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=context['depot'])
        return dict(list(context.items()) + list(c_def.items()))


# -- Adding objects --


class AddCity(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddCityForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('cities')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить город')
        return dict(list(context.items()) + list(c_def.items()))


class AddLine(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddLineForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('lines')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить линию')
        return dict(list(context.items()) + list(c_def.items()))


class AddStation(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddStationForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('stations')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить станцию')
        return dict(list(context.items()) + list(c_def.items()))


class AddTrain(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddTrainForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('trains')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить метровагон')
        return dict(list(context.items()) + list(c_def.items()))


class AddDepot(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddDepotForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('depots')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Добавить депо')
        return dict(list(context.items()) + list(c_def.items()))


# -- Editing objects --


class UpdateCity(LoginRequiredMixin, DataMixin, UpdateView):
    model = City
    form_class = AddCityForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'city_slug'
    context_object_name = 'model'

    success_url = reverse_lazy('cities')

    def form_valid(self, form):
        new_object = form.save(commit=False)
        if 'clear_image' in self.request.POST:
            new_object.image = None
        new_object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Редактировать город')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()


class UpdateLine(LoginRequiredMixin, DataMixin, UpdateView):
    model = Line
    form_class = AddLineForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'line_slug'
    context_object_name = 'model'

    success_url = reverse_lazy('lines')

    def form_valid(self, form):
        new_object = form.save(commit=False)
        if 'clear_image' in self.request.POST:
            new_object.image = None
        new_object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Редактировать линию')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()


class UpdateStation(LoginRequiredMixin, DataMixin, UpdateView):
    model = Station
    form_class = EditStationForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'station_slug'
    context_object_name = 'model'

    success_url = reverse_lazy('stations')

    def form_valid(self, form):
        new_object = form.save(commit=False)
        if 'clear_image' in self.request.POST:
            new_object.image = None
        new_object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        context['loading_message'] = True
        c_def = self.get_user_context(title='Редактировать станцию')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()


class UpdateTrain(LoginRequiredMixin, DataMixin, UpdateView):
    model = Train
    form_class = AddTrainForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'train_slug'
    context_object_name = 'model'

    success_url = reverse_lazy('trains')

    def form_valid(self, form):
        new_object = form.save(commit=False)
        if 'clear_image' in self.request.POST:
            new_object.image = None
        new_object.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Редактировать поезд')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()


class UpdateDepot(LoginRequiredMixin, DataMixin, UpdateView):
    model = Depot
    form_class = AddDepotForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'depot_slug'
    context_object_name = 'model'

    success_url = reverse_lazy('depots')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Редактировать депо')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        new_object = form.save(commit=False)
        if 'clear_image' in self.request.POST:
            new_object.image = None
        new_object.save()
        return super().form_valid(form)

    def get_queryset(self):
        return self.model.objects.all()


# -- delete objects --


class DeleteCity(LoginRequiredMixin, DataMixin, DeleteView):
    model = City
    template_name = 'wiki/delete-objects.html'
    slug_url_kwarg = 'city_slug'

    success_url = reverse_lazy('cities')
    login_url = reverse_lazy('login')

    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Удалить город')
        return dict(list(context.items()) + list(c_def.items()))


class DeleteLine(LoginRequiredMixin, DataMixin, DeleteView):
    model = Line
    template_name = 'wiki/delete-objects.html'
    slug_url_kwarg = 'line_slug'

    success_url = reverse_lazy('lines')
    login_url = reverse_lazy('login')

    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Удалить линию')
        return dict(list(context.items()) + list(c_def.items()))


class DeleteStation(LoginRequiredMixin, DataMixin, DeleteView):
    model = Station
    template_name = 'wiki/delete-objects.html'
    slug_url_kwarg = 'station_slug'

    success_url = reverse_lazy('stations')
    login_url = reverse_lazy('login')

    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Удалить станцию')
        return dict(list(context.items()) + list(c_def.items()))


class DeleteTrain(LoginRequiredMixin, DataMixin, DeleteView):
    model = Train
    template_name = 'wiki/delete-objects.html'
    slug_url_kwarg = 'train_slug'

    success_url = reverse_lazy('trains')
    login_url = reverse_lazy('login')

    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Удалить метровагон')
        return dict(list(context.items()) + list(c_def.items()))


class DeleteDepot(LoginRequiredMixin, DataMixin, DeleteView):
    model = Depot
    template_name = 'wiki/delete-objects.html'
    slug_url_kwarg = 'depot_slug'

    success_url = reverse_lazy('depots')
    login_url = reverse_lazy('login')

    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Удалить депо')
        return dict(list(context.items()) + list(c_def.items()))


# -- selectors --


class StationSelectorResult(DataMixin, ListView):
    template_name = 'wiki/search/stations.html'
    paginate_by = 128
    context_object_name = 'stations'

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        context['ordering'] = OrderingStationForm()
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=f'Результаты поиска: {self.request.GET.get("q")}')

        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Station.objects.filter(title__icontains=self.request.GET.get('q')) \
            .order_by(self.request.GET.get('ordering'), 'title') if self.request.GET.get('ordering') \
                                                                    != 'По алфавиту (По убиванию)' else Station.objects.filter(
            title__icontains=self.request.GET.get('q')) \
            .order_by(self.request.GET.get('ordering'))

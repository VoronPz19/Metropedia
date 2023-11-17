from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from metro_blog.models import Blog
from main_page.utils import DataMixin


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))


class EditUser(LoginRequiredMixin, DataMixin, UpdateView):
    model = Profile
    template_name = 'user/user_edit_form.html'
    pk_url_kwarg = 'profile_pk'
    form_class = EditingUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        context['form'] = EditingUserForm(instance=self.request.user)
        c_def = self.get_user_context(title='Настройки аккаунта')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationUserForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


class Account(LoginRequiredMixin, DataMixin, DetailView):
    model = Profile
    pk_url_kwarg = 'profile_pk'
    template_name = 'user/profile.html'
    context_object_name = 'user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count

        # pppc = (public post profile count)
        context['post_profile_count'] = Blog.objects.filter(owner=context['user']).count
        context['pppc'] = Blog.objects.filter(owner=context['user'], is_public=True).count
        context['post_user'] = Blog.objects.filter(owner=self.request.user)
        context['tracked_city_posts'] = Blog.objects.filter(city=self.request.user.tracked_city, is_public=True)
        context['posts'] = Blog.objects.filter(is_public=True)

        c_def = self.get_user_context(title=context['user'])
        return dict(list(context.items()) + list(c_def.items()))


class UserAccount(LoginRequiredMixin, DataMixin, ListView):
    model = Profile
    template_name = 'user/account.html'
    context_object_name = 'user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count

        # pppc = (public post profile count)
        context['pppc'] = Blog.objects.filter(owner=self.request.user, is_public=True).count
        context['post_user'] = Blog.objects.filter(owner=self.request.user)
        context['tracked_city_posts'] = Blog.objects.filter(city=self.request.user.tracked_city, is_public=True)
        context['posts'] = Blog.objects.filter(is_public=True)

        c_def = self.get_user_context(title=self.request.user)
        return dict(list(context.items()) + list(c_def.items()))

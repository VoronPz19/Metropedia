from django.shortcuts import redirect
from django.contrib.auth import login
from django.views.generic import ListView, CreateView
from .forms import *
from django.urls import reverse_lazy
from main_page.utils import DataMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main_page/register.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm

    template_name = 'main_page/login.html'
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


class Account(DataMixin, ListView):
    model = Blog
    template_name = 'main_page/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))
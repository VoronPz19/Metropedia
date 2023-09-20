from django.views.generic import ListView, DetailView
from .models import *

menu = [{'title': 'добавить статью', 'url_name': 'index'},
        {'title': 'Войти', 'url_name': 'index'},
        {'title': 'Статьи', 'url_name': 'index'}]


class Blogs(ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости о метрополитене'
        context['menu'] = menu
        return context


class ShowPost(DetailView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context

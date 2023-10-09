from django.views.generic import ListView, DetailView
from metro_blog.models import *
from main_page.utils import DataMixin, LastNewsMixin


class LastNews(DataMixin, LastNewsMixin, ListView):
    model = Blog
    template_name = 'main_page/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

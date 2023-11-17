from django.views.generic import ListView
from metro_blog.models import *
from main_page.utils import DataMixin


class LastNews(DataMixin, ListView):
    model = Blog
    template_name = 'main_page/index.html'
    context_object_name = 'posts'
    view_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Blog.objects.filter(is_public=True)[:self.view_by]
        context['count'] = Blog.objects.filter(is_public=True)[:self.view_by].count
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


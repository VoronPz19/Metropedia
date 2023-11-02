from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from django.urls import reverse_lazy
from main_page.utils import DataMixin


class Blogs(DataMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Blog.objects.filter(is_public=True)
        c_def = self.get_user_context(title='Новости')
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.all()
        context['comment_count'] = Comment.objects.count()
        context['form'] = CommentForm()
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse('request: post', kwargs={'slug': self.object.post.slug})

    def form_valid(self, form):
        form.instance.post = Request
        return super().form_valid(form)


class AddPost(DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main_page/forms.html'
    success_url = reverse_lazy('blogs')
    login_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Конструктор новостей')
        return dict(list(context.items()) + list(c_def.items()))

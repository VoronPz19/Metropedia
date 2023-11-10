from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from main_page.utils import DataMixin

from .forms import *


class PublicPosts(DataMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Blog.objects.filter(is_public=True)
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Новости')
        return dict(list(context.items()) + list(c_def.items()))


class AllPosts(DataMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = Blog.is_public
        context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Предложенные новости')
        return dict(list(context.items()) + list(c_def.items()))


class UserPosts(LoginRequiredMixin, DataMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Blog.objects.filter(owner=self.request.user)
        context['status'] = Blog.is_public
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        print(Blog.owner, self.request.user)
        c_def = self.get_user_context(title='Ваши новости')
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DetailView, DataMixin):
    model = Blog
    template_name = 'blog/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class AddComment(LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'metro_blog/post.html'
    form_class = CommentForm

    def form_valid(self, form):
        new_comment = form.save(commit=False)
        new_comment.owner = self.request.user
        new_comment.post = self.model
        new_comment.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Конструктор новостей')
        return dict(list(context.items()) + list(c_def.items()))


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'main_page/forms.html'
    form_class = AddPostForm
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.owner = self.request.user
        new_post.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Конструктор новостей')
        return dict(list(context.items()) + list(c_def.items()))


class UpdatePost(LoginRequiredMixin, DataMixin, UpdateView):
    model = Blog
    form_class = AddPostForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'post_slug'

    success_url = reverse_lazy('blogs')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Конструктор новостей')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class PublicPost(LoginRequiredMixin, DataMixin, UpdateView):
    model = Blog
    slug_url_kwarg = 'post_slug'
    extra_context = {'post': Blog.objects.all()}
    success_url = reverse_lazy('blogs')
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        c_def = self.get_user_context(title='Конструктор новостей')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.filter(owner=self.request.user)


class PostDelete(LoginRequiredMixin, DataMixin, DeleteView):
    model = Blog
    template_name = 'blog/delete-post.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('blogs')
    login_url = reverse_lazy('login')
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Удалить новость')
        return dict(list(context.items()) + list(c_def.items()))

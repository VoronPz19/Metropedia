from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
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
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        c_def = self.get_user_context(title='Новости')
        return dict(list(context.items()) + list(c_def.items()))


class AllPosts(DataMixin, ListView):
    model = Blog
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['status'] = True
        if self.request.user.is_authenticated:
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
        context['status'] = True
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


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    template_name = 'main_page/forms.html'
    form_class = AddPostForm

    success_url = reverse_lazy('blogs')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.owner = self.request.user
        if 'save_public' in self.request.POST:
            new_post.is_public = True
        new_post.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['public_form'] = True
        c_def = self.get_user_context(title='Конструктор новостей')
        return dict(list(context.items()) + list(c_def.items()))


class UpdatePost(LoginRequiredMixin, DataMixin, UpdateView):
    model = Blog
    form_class = AddPostForm
    template_name = 'main_page/forms.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'model'

    success_url = reverse_lazy('blogs')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        new_post = form.save(commit=False)
        if 'save_non_public' in self.request.POST:
            new_post.is_public = False
        if 'save_public' in self.request.POST:
            new_post.is_public = True
        if 'clear_image' in self.request.POST:
            new_post.image = None
        new_post.save()
        return super().form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['post_user_count'] = Blog.objects.filter(owner=self.request.user).count
        update = True
        context['update'] = update
        context['public_form'] = True
        c_def = self.get_user_context(title='Конструктор новостей')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return self.model.objects.all()


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

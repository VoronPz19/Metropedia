from django.db import models
from metro_wiki.models import *
from django.urls import reverse
from users.models import Profile
from ckeditor.fields import RichTextField


class Blog(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Автор')

    title = models.CharField(max_length=250, blank=False, verbose_name='Название')
    slug = models.CharField(max_length=250, unique=True, verbose_name='Ссылка')

    content = RichTextField(blank=True, null=True, verbose_name='Текст', config_name='extends')

    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')
    source = models.CharField(max_length=250, blank=True, null=True, verbose_name='Источник')

    is_public = models.BooleanField(default=False)

    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Город')
    line = models.ManyToManyField(Line, blank=True, verbose_name='линий')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_created']


class Comment(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Владелец')
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True, verbose_name='пост')
    text = models.TextField(max_length=500, blank=True, null=True, verbose_name='Текст')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-time_created']

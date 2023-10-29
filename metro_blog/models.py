from django.db import models
from metro_wiki.models import Line
from django.urls import reverse
from users.models import Profile
from ckeditor.fields import RichTextField


class Blog(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=250, blank=False, verbose_name='Название')
    slug = models.CharField(max_length=250, unique=True, verbose_name='Ссылка')
    content = RichTextField(blank=True, null=True, verbose_name='Текст', config_name='extends')
    source = models.CharField(max_length=250, blank=True, null=True, verbose_name='Источник')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')
    is_public = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    line = models.ForeignKey(Line, on_delete=models.PROTECT, blank=True, null=True, verbose_name='линия')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_created']

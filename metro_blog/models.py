from metro_wiki.models import *
from django.urls import reverse
from users.models import Profile
from ckeditor.fields import RichTextField

from main_page.utils import unique_slugify


class Blog(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Автор')

    title = models.CharField(max_length=250, blank=False, verbose_name='Название')
    slug = models.CharField(max_length=250, unique=True, verbose_name='Ссылка',
                            help_text='Оставьте поле пустым, чтобы сгенерировать автоматически')

    content = RichTextField(blank=True, null=True, verbose_name='Текст', config_name='extends')

    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')
    source = models.CharField(max_length=250, blank=True, null=True, verbose_name='Источник')

    is_public = models.BooleanField(default=False, verbose_name='Публичный')

    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    city = models.ForeignKey(City, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Город')
    line = models.ManyToManyField(Line, blank=True, verbose_name='линий')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_created']

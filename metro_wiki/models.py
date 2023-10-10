from django.db import models
from colorfield.fields import ColorField
from django.urls import reverse


class City(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название города')
    slug = models.CharField(max_length=100, blank=False, unique=True, verbose_name='Ссылка')
    info = models.TextField(blank=True, null=True, verbose_name='Текст')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cities', kwargs={'cities_slug': self.slug})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Line(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название линий')
    slug = models.CharField(max_length=100, blank=False, unique=True, verbose_name='Ссылка')
    number = models.CharField(max_length=3, blank=True, verbose_name='Номер линий')
    color = ColorField(default='#EF161E', verbose_name='Цвет линий')
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    info = models.TextField(blank=True, null=True, verbose_name='Текст')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('line', kwargs={'line_slug': self.slug})

    class Meta:
        verbose_name = 'Линия'
        verbose_name_plural = 'Линии'

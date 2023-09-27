from django.db import models
from colorfield.fields import ColorField


class City(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название города')
    slug = models.CharField(max_length=100, blank=False, unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Line(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название линий')
    slug = models.CharField(max_length=100, blank=False, unique=True, verbose_name='Ссылка')
    number = models.CharField(max_length=3, blank=True, verbose_name='Номер линий')
    color = ColorField(default='#EF161E', verbose_name='Цвет линий')
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Линия'
        verbose_name_plural = 'Линий'
        ordering = ['number']

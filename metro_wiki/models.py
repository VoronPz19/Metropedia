from django.db import models
from colorfield.fields import ColorField


class Line(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название линий')
    slug = models.CharField(max_length=100, blank=False, unique=True, verbose_name='Ссылка')
    number = models.CharField(max_length=3, blank=True, verbose_name='Номер линий')
    color = ColorField(default='#EF161E', verbose_name='Цвет линий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Линия'
        verbose_name_plural = 'Линий'
        ordering = ['number']

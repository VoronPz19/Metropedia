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


class CityInfo(models.Model):
    city = models.OneToOneField(City, on_delete=models.PROTECT, verbose_name='линия')
    info = models.TextField(blank=True, null=True, verbose_name='Текст')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Информация о городе'
        verbose_name_plural = 'Информация о городе'


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
        verbose_name_plural = 'Линии'


class LineInfo(models.Model):
    line = models.OneToOneField(Line, on_delete=models.PROTECT, verbose_name='линия')
    info = models.TextField(blank=True, null=True, verbose_name='Текст')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.line

    class Meta:
        verbose_name = 'Информация о линий'
        verbose_name_plural = 'Информация о линий'

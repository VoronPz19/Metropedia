from django.db import models
from colorfield.fields import ColorField
from django.urls import reverse
from ckeditor.fields import RichTextField

from main_page.utils import unique_slugify


class City(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название метрополитена')
    slug = models.CharField(max_length=100, blank=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')
    content = RichTextField(blank=True, null=True, verbose_name='Текст', config_name='extends')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('city', kwargs={'city_slug': self.slug})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['title']


class Line(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Название линий')
    slug = models.CharField(max_length=100, blank=True, unique=True, verbose_name='Ссылка')
    content = RichTextField(blank=True, null=True, verbose_name='Текст', config_name='extends')
    number = models.CharField(max_length=3, blank=True, verbose_name='Номер линий')
    color_text = ColorField(default='#FFFFFF', verbose_name='Цвет текста')
    color = ColorField(default='#EF161E', verbose_name='Цвет')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('line', kwargs={'line_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Линия'
        verbose_name_plural = 'Линии'
        ordering = ['number', 'title']


class Station(models.Model):
    STATUS_TYPE = (
        ('Эксплуатируется', '🚇 Эксплуатируется'),
        ('Строится', '🛠️ Строится'),
        ('Проектируется', '✏ Проектируется'),
        ('Планируется', '📄 Планируется'),
        ('Закрыта', '🔒 Закрыта'),
    )

    PATH_TYPE = (
        ('Эксплуатируется', '🚇 Эксплуатируется'),
        ('Строится', '🛠️ Строится'),
        ('Ничего', 'Ничего'),
    )

    PATH_DIRECTION = (
        ('Основной путь', 'Основной путь'),
        ('Ответвление', 'Ответвление'),
        ('Начало ответвления', 'Начало ответвления'),
        ('Конец ответвления', 'Конец ответвления'),
    )

    title = models.CharField(max_length=100, blank=False, verbose_name='Название станций')
    slug = models.CharField(max_length=100, blank=True, unique=True, verbose_name='Ссылка')
    content = RichTextField(blank=True, null=True, verbose_name='Текст', config_name='extends')
    index = models.IntegerField(default=1, verbose_name='Номер станций (север-юг/восток-запад)')
    transfer = models.ManyToManyField('Station', blank=True, related_name='+', verbose_name='Пересадки',
                                      help_text='После добавления пересадок, вам нужно ещё раз сохранить станцию')
    path_direction = models.CharField(max_length=200, choices=PATH_DIRECTION,
                                      default='Основной путь', verbose_name='Тип пути')
    prev_path = models.CharField(max_length=200, choices=PATH_TYPE,
                                 default='Эксплуатируется', verbose_name='Путь к предыдущей станций')
    status = models.CharField(max_length=200, choices=STATUS_TYPE, default='Эксплуатируется', verbose_name='Статус')
    next_path = models.CharField(max_length=200, choices=PATH_TYPE,
                                 default='Эксплуатируется', verbose_name='Путь к следующей станций')
    line = models.ForeignKey(Line, on_delete=models.PROTECT, verbose_name='Линия')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')

    def __str__(self):
        return f'{self.title} - {self.line.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('station', kwargs={'station_slug': self.slug})

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станций'
        ordering = ['line', 'index', 'title']


class Train(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Модель метровагона')
    slug = models.CharField(max_length=100, blank=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')
    content = RichTextField(blank=True, null=True, verbose_name='Текст', config_name='extends')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('train', kwargs={'train_slug': self.slug})

    class Meta:
        verbose_name = 'Метровагон'
        verbose_name_plural = 'Метровагоны'
        ordering = ['title']


class Depot(models.Model):
    STATUS_TYPE = (
        ('Эксплуатируется', '🚇 Эксплуатируется'),
        ('Строится', '🛠️ Строится'),
        ('Проектируется', '✏ Проектируется'),
        ('Планируется', '📄 Планируется'),
        ('Закрыта', '🔒 Закрыта'),
    )

    number_of_depot = models.IntegerField(default=1, verbose_name='Номер депо')
    title = models.CharField(max_length=100, blank=False, verbose_name='Название депо')
    slug = models.CharField(max_length=100, blank=True, unique=True, verbose_name='Ссылка')
    image = models.ImageField(upload_to='images/%Y/%M/%D', blank=True, verbose_name='Картинка')
    content = RichTextField(blank=True, null=True, verbose_name='Текст', config_name='extends')
    status = models.CharField(max_length=200, choices=STATUS_TYPE, default='Эксплуатируется', verbose_name='Статус')
    index = models.IntegerField(default=0, verbose_name='Номер станций под которым находится',
                                help_text='Укажите 0, чтобы депо отображалось сверху')
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Город')
    main_line = models.ForeignKey(Line, on_delete=models.CASCADE, null=True,
                                  verbose_name='Линия на котором она расположена')
    lines = models.ManyToManyField(Line, blank=True, related_name='+', verbose_name='Другие обслуживаемые линии')
    trains = models.ManyToManyField(Train, blank=True, related_name='+', verbose_name='Поезда')

    def __str__(self):
        return f'ТЧ-{self.number_of_depot} {self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slugify(self, self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('depot', kwargs={'depot_slug': self.slug})

    class Meta:
        verbose_name = 'Депо'
        verbose_name_plural = 'Депо'
        ordering = ['city', 'number_of_depot']

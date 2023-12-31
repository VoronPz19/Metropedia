# Generated by Django 4.2.5 on 2023-11-07 13:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metro_wiki', '0023_alter_city_content_alter_line_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Модель метровагона')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%M/%D', verbose_name='Картинка')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Метровагон',
                'verbose_name_plural': 'Метровагоны',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Depot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Модель метровагона')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%M/%D', verbose_name='Картинка')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Текст')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='metro_wiki.city', verbose_name='Город')),
                ('lines', models.ManyToManyField(blank=True, related_name='+', to='metro_wiki.line', verbose_name='Обслуживаемые линий')),
                ('trains', models.ManyToManyField(blank=True, related_name='+', to='metro_wiki.train', verbose_name='Поезда')),
            ],
            options={
                'verbose_name': 'Депо',
                'verbose_name_plural': 'Депо',
                'ordering': ['title'],
            },
        ),
    ]

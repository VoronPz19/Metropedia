# Generated by Django 4.2.5 on 2023-11-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro_blog', '0009_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(help_text='Оставьте поле пустым, чтобы сгенерировать автоматически', max_length=250, unique=True, verbose_name='Ссылка'),
        ),
    ]
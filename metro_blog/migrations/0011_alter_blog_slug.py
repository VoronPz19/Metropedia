# Generated by Django 4.2.5 on 2023-11-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro_blog', '0010_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=250, unique=True, verbose_name='Ссылка'),
        ),
    ]

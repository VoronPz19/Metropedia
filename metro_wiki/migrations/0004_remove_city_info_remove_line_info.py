# Generated by Django 4.2.5 on 2023-10-13 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metro_wiki', '0003_remove_lineinfo_line_city_image_city_info_line_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='info',
        ),
        migrations.RemoveField(
            model_name='line',
            name='info',
        ),
    ]

# Generated by Django 4.2.5 on 2023-11-10 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metro_wiki', '0028_alter_depot_lines_alter_depot_main_line'),
        ('users', '0004_profile_city_profile_tracked_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tracked_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='metro_wiki.city', verbose_name='Отслеживаемый метрополитен'),
        ),
    ]
# Generated by Django 4.2.5 on 2023-11-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro_wiki', '0024_train_depot'),
    ]

    operations = [
        migrations.AddField(
            model_name='depot',
            name='index',
            field=models.IntegerField(default=0, help_text='Укажите 0, чтобы депо отображалось сверху', verbose_name='Номер станций под которым находится'),
        ),
    ]
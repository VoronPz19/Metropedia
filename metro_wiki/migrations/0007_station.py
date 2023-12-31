# Generated by Django 4.2.5 on 2023-10-22 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metro_wiki', '0006_line_color_text_alter_city_title_alter_line_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название линий')),
                ('slug', models.CharField(max_length=100, unique=True, verbose_name='Ссылка')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Текст')),
                ('status', models.CharField(choices=[('🛠️ Строящиеся', 'Строящиеся'), ('🚇 Эксплуатируйся', 'Эксплуатируйся'), ('📄 Проектируемая', 'Проектируемая'), ('🔒 Закрытая', 'Закрытая')], max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%M/%D', verbose_name='Картинка')),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='metro_wiki.line')),
            ],
            options={
                'verbose_name': 'Станция',
                'verbose_name_plural': 'Станций',
            },
        ),
    ]

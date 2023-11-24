from django.apps import AppConfig


class MetroWikiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'metro_wiki'
    verbose_name = 'Информация о метрополитене'

    def ready(self):
        import metro_wiki.signals

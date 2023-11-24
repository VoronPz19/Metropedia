from uuid import uuid4
from pytils.translit import slugify


def unique_slugify(instance, slug):
    model = instance.__class__
    unique_slug = slugify(slug)

    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{uuid4().hex[:8]}'
    return unique_slug


menu = [{'title': 'Главная страница', 'url_name': 'main'},
        {'title': 'Новости метрополитена', 'url_name': 'blogs'}]

submenu_editor = [{'title': '__object_line_hr__'},
                  {'title': 'Добавить город', 'url_name': 'add_city'},
                  {'title': 'Добавить линию', 'url_name': 'add_line'},
                  {'title': 'Добавить станцию', 'url_name': 'add_station'},
                  {'title': 'Добавить Состав', 'url_name': 'add_train'},
                  {'title': 'Добавить Депо', 'url_name': 'add_depot'},
                  {'title': '__object_line_hr__'},
                  {'title': 'Добавить новость', 'url_name': 'add_post'},
                  {'title': 'Посмотреть предложенные новости', 'url_name': 'post_list'},
                  {'title': '__object_line_hr__'},]

cats = [{'title': 'Города', 'url_name': 'cities', 'image': 'images/cities.jpg'},
        {'title': 'Линий', 'url_name': 'lines', 'image': 'images/lines.jpg'},
        {'title': 'Станций', 'url_name': 'stations', 'image': 'images/stations.jpg'},
        {'title': 'Метровагоны', 'url_name': 'trains', 'image': 'images/trains.jpg'},
        {'title': 'Депо', 'url_name': 'depots', 'image': 'images/depots.jpg'}]


class DataMixin:

    @staticmethod
    def get_user_context(**kwargs):
        context = kwargs

        context['menu'] = menu
        context['submenu_editor'] = submenu_editor
        context['cats'] = cats

        return context

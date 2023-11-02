menu = [{'title': 'Главная страница', 'url_name': 'main'},
        {'title': 'Новости метрополитена', 'url_name': 'blogs'}]

submenu = [{'title': 'Добавить город', 'url_name': 'add_city'},
           {'title': 'Добавить линию', 'url_name': 'add_line'},
           {'title': 'Добавить станцию', 'url_name': 'add_station'},
           {'title': 'Добавить новость', 'url_name': 'add_post'},
           {'title': 'Посмотреть предложенные новости', 'url_name': 'post_list'}]

cats = [{'title': 'Города', 'url_name': 'cities', 'image': 'images/cities.jpg'},
        {'title': 'Линий', 'url_name': 'lines', 'image': 'images/lines.jpg'},
        {'title': 'Станций', 'url_name': 'stations', 'image': 'images/stations.jpg'}]


class DataMixin:

    @staticmethod
    def get_user_context(**kwargs):
        context = kwargs

        context['menu'] = menu
        context['submenu'] = submenu
        context['cats'] = cats

        return context


class LastNewsMixin:
    paginate_by = 5

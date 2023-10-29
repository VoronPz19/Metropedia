menu = [{'title': 'Главная страница', 'url_name': 'main'},
        {'title': 'Новости метрополитена', 'url_name': 'blogs'},
        {'title': 'Предложить новость', 'url_name': 'main'}]

cats = [{'title': 'Города', 'url_name': 'cities', 'image': 'images/cities.jpg'},
        {'title': 'Линий', 'url_name': 'lines', 'image': 'images/lines.jpg'},
        {'title': 'Станций', 'url_name': 'stations', 'image': 'images/stations.jpg'}]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(-1)
        if self.request.user.is_staff:
            user_menu.append({'title': 'Добавить станцию', 'url_name': 'add_station'})
        context['menu'] = user_menu
        context['cats'] = cats

        return context


class LastNewsMixin:
    paginate_by = 5

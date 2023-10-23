menu = [{'title': 'Информация метрополитена', 'url_name': 'main'},
        {'title': 'Новости метрополитена', 'url_name': 'blogs'},
        {'title': 'Предложить новость', 'url_name': 'main'}]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(-1)
        context['menu'] = user_menu

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


class LastNewsMixin:
    paginate_by = 5

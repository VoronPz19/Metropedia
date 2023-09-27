menu = [{'title': 'Информация метрополитена', 'url_name': 'main'},
        {'title': 'Новости метрополитена', 'url_name': 'blogs'},
]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
        context['menu'] = user_menu

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

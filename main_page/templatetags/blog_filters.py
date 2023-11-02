from django import template


register = template.Library()


@register.filter
def replacer(text):
    filtration = {'&ndash;': '-', '&laquo;': '«', '&raquo;': '»', '&nbsp;': ' \n'}

    for key, value in filtration.items():
        text = text.replace(key, value)

    return text

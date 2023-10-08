from django import template


register = template.Library()


@register.filter
def replace_ndash(value):
    return value.replace('&ndash;', '-')

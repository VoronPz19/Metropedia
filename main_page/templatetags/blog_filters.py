from django import template


register = template.Library()


@register.filter
def replace_ndash(value):
    return value.replace('&ndash;', '-')


@register.filter
def replace_aquo(value):
    return value.replace('&laquo;', '«').replace('&raquo;', '»')


@register.filter
def replace_nbsp(value):
    return value.replace('&nbsp;', ' \n')

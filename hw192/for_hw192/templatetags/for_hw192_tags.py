from django import template


register = template.Library()


@register.filter()
def mediapath(val):
    if val:
        return f'for_hw192/images/{val}'

    return '#'
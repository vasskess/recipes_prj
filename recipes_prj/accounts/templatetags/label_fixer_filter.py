from django.template import Library

register = Library()


@register.filter("fix_label")
def field_fix(value):
    value = value.replace('_', ' ')
    return value.title()

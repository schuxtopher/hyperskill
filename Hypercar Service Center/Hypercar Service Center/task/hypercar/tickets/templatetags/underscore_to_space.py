from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def underscore_to_space(value):
    return value.replace('_', ' ')

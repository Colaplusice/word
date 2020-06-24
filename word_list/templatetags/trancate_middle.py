"""
@time: 2020-06-23 15:50
@author: colaplusice
@contact: fjl2401@163.com vx:18340071291
"""

from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()


@register.filter(is_safe=True)
@stringfilter
def truncatechars_middle(value, arg):
    try:
        ln = int(arg)
    except ValueError:
        return value
    if len(value) <= ln:
        return value
    else:
        return '{}...{}'.format(value[:ln-2], value[-2:])

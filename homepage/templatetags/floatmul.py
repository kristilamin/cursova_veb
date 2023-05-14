from django import template

register = template.Library()

@register.filter
def floatmul(value, arg):
    return float(value) * float(arg)
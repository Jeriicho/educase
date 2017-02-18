from django import template

register = template.Library()

@register.filter
def toStr(arg):
    return str(arg)
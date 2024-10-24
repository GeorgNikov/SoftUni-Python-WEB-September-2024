from django import template

register = template.Library()

@register.filter
def split_by_comma(value):
    """Splits the input string by ', ' (comma and space)"""
    return value.split(', ')
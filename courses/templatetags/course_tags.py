from django import template

register = template.Library()

@register.filter
def split_lines(value):
    if not value:
        return []
    lines = [line.strip() for line in value.replace('\r', '').split('\n') if line.strip()]
    if not lines:
        lines = [line.strip() for line in value.split(',') if line.strip()]
    return lines

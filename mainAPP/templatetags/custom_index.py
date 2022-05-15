from django import template
register = template.Library()

@register.filter('custom_index')
def custom_index(indexable, pid):
    for entry in indexable:
        if entry.pid.pid == pid:
            return entry.points
    return 0.0
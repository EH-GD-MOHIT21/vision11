from django import template
register = template.Library()

@register.filter('custom_index_captain')
def custom_index_captain(indexable, pid):
    for entry in indexable:
        if entry.pid.pid == pid:
            return entry.points*2
    return 0.0
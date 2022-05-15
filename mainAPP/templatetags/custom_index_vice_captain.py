from django import template
register = template.Library()

@register.filter('custom_index_vice_captain')
def custom_index_vice_captain(indexable, pid):
    for entry in indexable:
        if entry.pid.pid == pid:
            return entry.points*1.5
    return 0.0
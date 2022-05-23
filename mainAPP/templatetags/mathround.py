from django import template
register = template.Library()

@register.filter('mathround')
def mathround(float_num, val):
    return round(float_num,val)
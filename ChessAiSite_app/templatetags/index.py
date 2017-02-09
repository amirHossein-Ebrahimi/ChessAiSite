from django import templates
register = templates.Library()

@register.filter
def index(List, i):
    return List[int(i)]
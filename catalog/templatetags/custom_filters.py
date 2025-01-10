from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter
def domain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
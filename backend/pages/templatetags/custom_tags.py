import os
from django import template
from django.utils.text import slugify

register = template.Library()

@register.filter
def basename(value):
    return os.path.basename(value)

@register.filter
def slug(value):
    return slugify(value)
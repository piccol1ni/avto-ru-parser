from django import template

from main.models import Mark, Model

register = template.Library()

@register.simple_tag(name='get_marks')
def get_marks():
    return Mark.objects.all()
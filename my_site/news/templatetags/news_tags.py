from django import template
from django.db.models import Count
from news.models import Category

register = template.Library()


@register.simple_tag
def get_categories():
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return categories


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)

    return {"categories": categories}

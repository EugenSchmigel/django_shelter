from django.core import cache

from config.settings import CACHE_ENABLED
from dog_.models import Category

def cache_category():
    if CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list
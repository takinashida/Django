from catalog.models import Product
from django.core.cache import cache
from fishgramm.settings import CACHE_ENABLED


def get_category_cache(category_pk):
    if not CACHE_ENABLED:
        return Product.objects.all().filter(is_published=True, category=category_pk)
    queryset = cache.get(f"category_queryset:{category_pk}")
    if queryset is not None:
        return queryset
    queryset = Product.objects.all().filter(is_published=True, category=category_pk)
    cache.set(f"category_queryset:{category_pk}", queryset, 60)
    return queryset

def get_products_cache():
    if not CACHE_ENABLED:
        return Product.objects.all().filter(is_published=True)
    queryset = cache.get("products_queryset")
    if queryset is not None:
        return queryset
    queryset = Product.objects.all().filter(is_published=True)
    cache.set("products_queryset", queryset, 60)
    return queryset
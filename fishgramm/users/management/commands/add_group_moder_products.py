from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        unpublish_product = Permission.objects.get(codename="can_unpublish_product")
        delete_product = Permission.objects.get(codename="delete_product")
        moderator_products = Group.objects.create(name="moderator_products")
        moderator_products.permissions.add(unpublish_product, delete_product)


from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.files import File
from pathlib import Path



class Command(BaseCommand):
    help = 'Add Products and Categories to database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category1, _ =Category.objects.get_or_create(name='Овощи', description='Полезные и питательные')
        category2, _ =Category.objects.get_or_create(name='Фрукты', description='Сладкие и вкусные')

        path = Path('fishgramm/media/contents/image/')
        with open(path / 'apple.png', 'rb') as f1,\
            open(path / 'pineapple.png', 'rb') as f2,\
            open(path / 'cabbage.png', 'rb') as f3,\
            open(path / 'corn.png', 'rb') as f4:
            products = [
            {'name':'Яблоко', 'description': 'Зеленое', 'img': File(f1), 'category': category2, 'price': 100},
            {'name': 'Ананас', 'description': 'Колючий', 'img': File(f2), 'category': category2, 'price': 200},
            {'name': 'Капуста', 'description': 'Укутанная', 'img': File(f3), 'category': category1, 'price': 80},
            {'name': 'Кукуруза', 'description': 'Желтая', 'img': File(f4), 'category': category1, 'price': 120}
             ]
            for product_data in products:
                product, created = Product.objects.get_or_create(**product_data)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Succcessfully added product: {product.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))





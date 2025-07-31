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
            open(path / 'cabbage.png', 'rb') as f3, \
            open(path / 'corn.png', 'rb') as f4, \
            open(path / 'Pear.jpg', 'rb') as f5, \
            open(path / 'abrikos.jpeg', 'rb') as f6, \
            open(path / 'Tomats.jpg', 'rb') as f7:
            products = [
            {'name':'Яблоко', 'description': 'Зеленое', 'img': File(f1), 'category': category2, 'price': 100},
            {'name': 'Ананас', 'description': 'Колючий', 'img': File(f2), 'category': category2, 'price': 200},
            {'name': 'Капуста', 'description': 'Укутанная', 'img': File(f3), 'category': category1, 'price': 80},
            {'name': 'Кукуруза', 'description': 'Желтая', 'img': File(f4), 'category': category1, 'price': 120},
            {'name': 'Груша', 'description': 'Ламповидная', 'img': File(f5), 'category': category2, 'price': 250},
            {'name': 'Абрикос', 'description': 'Ядровой', 'img': File(f6), 'category': category2, 'price': 180},
            {'name': 'Томат', 'description': 'Коктельные', 'img': File(f7), 'category': category1, 'price': 110}
             ]
            for product_data in products:
                product, created = Product.objects.get_or_create(**product_data)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))


import os.path
from email.policy import default

from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.core.files import File
from pathlib import Path

from fishgramm.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = 'Add Products and Categories to database'

    def handle(self, *args, **kwargs):
        for product in Product.objects.all():
            if product.img:
                product.img.delete(save=False)
        Category.objects.all().delete()
        Product.objects.all().delete()

        category1, _ = Category.objects.get_or_create(name='Овощи', description='Полезные и питательные')
        category2, _ = Category.objects.get_or_create(name='Фрукты', description='Сладкие и вкусные')

        base_path = Path.joinpath(MEDIA_ROOT, 'contents', 'image')

        products = [
        {'name':'Яблоко', 'description': 'Зеленое', 'filename': 'apple.png', 'category': category2, 'price': 100},
        {'name': 'Ананас', 'description': 'Колючий', 'filename': 'pineapple.png', 'category': category2, 'price': 200},
        {'name': 'Капуста', 'description': 'Укутанная', 'filename': 'cabbage.png', 'category': category1, 'price': 80},
        {'name': 'Кукуруза', 'description': 'Желтая', 'filename': 'corn.png', 'category': category1, 'price': 120},
        {'name': 'Груша', 'description': 'Ламповидная', 'filename': 'Pear.jpg', 'category': category2, 'price': 250},
        {'name': 'Абрикос', 'description': 'Ядровой', 'filename': 'abrikos.jpeg', 'category': category2, 'price': 180},
        {'name': 'Томат', 'description': 'Коктельные', 'filename': 'Tomats.jpg', 'category': category1, 'price': 110}
         ]
        for product_data in products:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'category': product_data['category'],
                    'price': product_data['price']
                }

            )
            path_to_img =Path.joinpath(base_path, product_data['filename'])
            with open(path_to_img, 'rb') as f:
                img_file = File(f)
                if product.img:
                    product.img.delete(save=False)
                    product.img.save(os.path.basename(path_to_img), img_file, save=True)
                else:
                    product.img.save(os.path.basename(path_to_img), img_file, save=True)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))


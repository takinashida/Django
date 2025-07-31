from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        ordering = ['name']

class Product(models.Model):

    name = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    img = models.ImageField(upload_to='contents/image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ['name']

class Contacts(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    email = models.CharField(max_length=100, verbose_name="email")
    message = models.TextField(verbose_name="Текст")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"
        ordering = ['email']
from django import forms

from catalog.models import Category


class ProductForm(forms.Form):
    name=forms.CharField(max_length=100, label="Название")
    description=forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Описание")
    img=forms.ImageField()
    price=forms.IntegerField(label="Цена")
    category=forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Выберите категорию")





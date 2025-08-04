from django import forms
from catalog.models import Category

class ProductForm(forms.Form):
    name = forms.CharField(max_length=150, label="Название")
    description = forms.CharField(widget=forms.Textarea({'cols': 60, 'rows': 10}), label="Описание")
    img = forms.ImageField(label="Фотография")
    price = forms.IntegerField(label="Цена")
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Выберите категорию")


class ContactsForm(forms.Form):
    name = forms.CharField(max_length=150, label="Имя")
    email = forms.CharField(max_length=150, label="Email")
    text = forms.CharField(widget=forms.Textarea({'cols': 60, 'rows': 10}), label="Описание")

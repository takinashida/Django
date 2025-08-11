from django import forms
from catalog.models import Category, Product, Contacts
from django.core.exceptions import ValidationError

# class StyleFormMixin:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'img', 'price', 'category']

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for bad_word in self.bad_words:
            if bad_word.lower() in name.lower():
                self.add_error('name', f"В названии содержатся запрещеные слова! {bad_word}")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for bad_word in self.bad_words:
            if bad_word.lower() in description.lower():
                raise ValidationError( f"В описании содержатся запрещеные слова! {bad_word}")
        return description

    def clean_img(self):
        img = self.cleaned_data.get("img")
        if img.size >= (5 * 1024 * 1024):
            raise ValidationError(f"Вес изображения не должен превышать 5 МБ")
        return img

    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get("price")
        if price < 0:
            self.add_error("price", "Цена не должна быть отрицательной")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.bad_words = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар'
        ]

        self.fields["name"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите название продукта:"
        })

        self.fields["description"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите описание продукта:"
        })

        self.fields["img"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Загрузите изображение продукта:"
        })

        self.fields["price"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите цену продукта:"
        })

        self.fields["category"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите категорию:"
        })





class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'message']
    # name = forms.CharField(max_length=150, label="Имя")
    # email = forms.CharField(max_length=150, label="Email")
    # message = forms.CharField(widget=forms.Textarea({'cols': 60, 'rows': 10}), label="Описание")




class ModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_published']

    def __init__(self, *args, **kwargs):
        super(ModeratorForm, self).__init__(*args, **kwargs)
        self.bad_words = [
            'казино',
            'криптовалюта',
            'крипта',
            'биржа',
            'дешево',
            'бесплатно',
            'обман',
            'полиция',
            'радар'
        ]

        self.fields['is_published'].widget.attrs.update({
            'class': 'form-check-input'
        })
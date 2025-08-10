from django.contrib.auth.forms import UserCreationForm
from users.models import User
from django import forms



class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
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

        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите свой email:"
        })

        self.fields["password1"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите пароль:"
        })

        self.fields["password2"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Повторите пароль:"
        })

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "phone_number", "avatar", "country"]

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
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

        self.fields["email"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите свой email:"
        })

        self.fields["phone_number"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Введите номер телефона(необязательно):"
        })

        self.fields["avatar"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Подгрузите картинку(необязательно):"
        })

        self.fields["country"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Укажите страну(необязательно):"
        })



import secrets

from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls.base import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from users.models import User
from users.forms import UserRegisterForm, UserChangeForm

from fishgramm.settings import EMAIL_HOST_USER



class RegistrationView(CreateView):
    model=User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        url = f"http://{self.request.get_host()}/email-confirm/{token}/"
        send_mail(
            subject='Подтверждение почты',
            message=f"Для подтверждения почты перейдите по ссылке: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))

class ProfileView(DetailView):
    model=User
    template_name = "users/profile.html"

class ChangeProfileView(UpdateView):
    model=User
    form_class = UserChangeForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        return self.request.user




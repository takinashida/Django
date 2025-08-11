from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from math import ceil

from django.http.response import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from catalog.forms import ProductForm, ContactsForm, ModeratorForm
from catalog.models import Product, Contacts
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class HomeView(View):
    def get(self, request):
        return render(request, "catalog/home.html")



class ContactsSuccessView(View):
    def get(self, request):
        return render(request, "catalog/contacts_success.html")

class ContactsCreateView(CreateView):
    model = Contacts
    form_class = ContactsForm
    template_name = 'catalog/contacts_form.html'
    success_url = reverse_lazy("catalog:contacts_success")

class ProductListView(ListView):
    model = Product
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        print("POST data:", self.request.POST)  # Что пришло от формы?
        print("Form data before validation:", form.data)  # Данные до clean()
        print("Form errors:", form.errors)
        return super().form_valid(form)



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:product_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ModeratorForm
        raise PermissionDenied

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    permission_required = 'catalog.delete_product'

    def form_valid(self, form):
        if not (self.request.user.has_perm(self.permission_required) or form.instance.owner==self.request.user):
            return HttpResponseForbidden("У вас нет прав доступа для удаления этого объекта")
        if self.object.img:
            self.object.img.delete(save=False)
        return super().form_valid(form)



# Create your views here.

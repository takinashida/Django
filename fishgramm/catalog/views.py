from django.http import HttpResponse
from math import ceil
from django.shortcuts import render
from catalog.forms import ProductForm, ContactsForm
from catalog.models import Product, Contacts
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views import View

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

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:product_list")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:product_list")

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")





# Create your views here.

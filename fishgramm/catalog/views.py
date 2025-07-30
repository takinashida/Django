from django.http import HttpResponse
from math import ceil
from django.shortcuts import render
from catalog.forms import ProductForm
from catalog.models import Product, Contacts


def home(request):
    products = Product.objects.order_by('created_at')[:5]
    for product in products:
        print(product)
    return render(request, "home.html", {'products': products})

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name"),
        email = request.POST.get("email"),
        message = request.POST.get("message")
        Contacts.objects.get_or_create(name=name,
                                       email=email,
                                       message=message)
        return HttpResponse(f"Спасибо, {name[0]}! Ваше сообщение получено.")
    return render(request, "contacts.html")

def catalog_page(request, page):
    per_page = 6
    products = Product.objects.all()
    if 1 <= page <= ceil(products.count()/per_page):
        start_product = (page - 1) * 6
        end_product = start_product+6
        if ceil(products.count()/per_page)*page > len(products):
            end_product = len(products)
        return render(
                request, "catalog_page.html",
        {'products':products[start_product:end_product]}
                          )
    return HttpResponse(404)

def product(request, id):
    product = Product.objects.get(id=id)
    return render(
        request, "product.html",
        {'product': product}
    )



def add_product(request):
    form = ProductForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            Product.objects.create(
                name= form.cleaned_data["name"],
                description = form.cleaned_data["description"],
                img = form.cleaned_data["img"],
                price = form.cleaned_data["price"],
                category = form.cleaned_data["category"],
            )
            return HttpResponse(f"Спасибо! Ваше сообщение получено.")
        else:
            return HttpResponse(f"Проверьте ваши данные.")
    return render(request, "add_product.html", {'form': form})



# Create your views here.

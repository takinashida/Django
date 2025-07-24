from django.http import HttpResponse

from django.shortcuts import render

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


# Create your views here.

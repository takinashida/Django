from django.http import HttpResponse

from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, "contacts.html")


# Create your views here.

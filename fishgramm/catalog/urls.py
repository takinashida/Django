from django.contrib import admin
from django.urls import path, include
from catalog.apps import BlogConfig
from catalog.views import home, contacts

app_name = BlogConfig.name

urlpatterns = [
    path('', home, name='index'),
    path('contacts/', contacts, name='contacts')
]


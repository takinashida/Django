from django.contrib import admin
from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, catalog_page, add_product



app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('catalog_page/<int:page>', catalog_page, name='catalog_page'),
    path('add_product/', add_product, name='add_product')
]


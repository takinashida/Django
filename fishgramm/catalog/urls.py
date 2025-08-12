from linecache import cache

from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView,\
    ContactsCreateView, HomeView, ContactsSuccessView, ping, CategoryListView
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('catalog/contacts/', ContactsCreateView.as_view(), name='contacts'),
    path('catalog/contacts/contacts_success', ContactsSuccessView.as_view(), name='contacts_success'),
    path('catalog/product_list/', ProductListView.as_view(), name='product_list'),
    path('catalog/product_detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('catalog/product_form/', ProductCreateView.as_view(), name='product_form'),
    path('catalog/product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/product_confirm_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('catalog/category_list/<int:category_pk>/', CategoryListView.as_view(), name='category_list'),
]


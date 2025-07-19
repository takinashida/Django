from django.contrib import admin
from django.urls import path, include
from blog.apps import BlogConfig
from blog.views import home, contacts

app_name = BlogConfig.name

urlpatterns = [
    path('', home, name='index'),
    path('contacts/', contacts, name='contacts')
]


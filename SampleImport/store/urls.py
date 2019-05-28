from django.contrib import admin
from django.urls import path, include
from .views import list_products, detail_product

urlpatterns = [
    path('', list_products, name= 'list_products'),
    path('<int:id>', detail_product, name= 'detail_product' ),
]

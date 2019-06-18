from django.contrib import admin
from django.urls import path, include, re_path
from .views import list_products, detail_product, list_products_by_marca, ProductoAPIList, ProductFilterAPIList

urlpatterns = [
    path('', list_products, name= 'list_products'),
    path('<int:id>', detail_product, name= 'detail_product' ),
    re_path('^(?P<category>.+)$', list_products_by_marca, name="products_brand"),
    #APIS
    path('api', ProductoAPIList.as_view(), name = "products_api" ),
    re_path('^api/(?P<category>.+)/(?P<brand>.+)/$', ProductFilterAPIList.as_view(), name="productsfilter_api"),
]

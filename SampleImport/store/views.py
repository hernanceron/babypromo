from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from .models import Product, Type, Brand, Store, Price
from datetime import date

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .serializers import ProductSerializer

from django.views import generic

import logging

logger = logging.getLogger(__name__)
# Create your views here.
def list_products(request):
    context = {}    
    tipoProductos = Type.objects.all()
    brands = Brand.objects.all()    
    stores = Store.objects.all()

    context['tipoProductos'] = tipoProductos
    context['brands'] = brands
    context['stores'] = stores
    
    products_list = Product.objects.all().order_by("name")

    paginator = Paginator(products_list,10)
    page = request.GET.get('page')   

    products = paginator.get_page(page)
    context['products'] = products
    logger.warn("Entrando a list_products")
    return render(request, 'store/products.html', context)

def detail_product(request,id):
    context = {}
    idProducto = id
    producto = get_object_or_404(Product, id = idProducto )
    prices = Price.objects.filter(product__id = idProducto, published_date = date.today())
    context['producto'] = producto
    if prices:
        context['prices'] = prices

    return render(request, 'store/product.html', context)

def list_products_by_marca(request, category):
    logger.warn("Entrando a list_products_by_marca")
    context = {}
    tipoProductos = Type.objects.all()
    stores = Store.objects.all()

    #idBrand = request.GET.get('idbrand')
    logger.warn("IdBrand : " + category)
    
    brands = Brand.objects.filter(name = category)

    products_list = get_list_or_404(Product, model__brand__name = category)

    paginator = Paginator(products_list,10)
    page = request.GET.get('page')   

    products = paginator.get_page(page)
    
    context['products'] = products
    context['brands'] = brands
    
    context['tipoProductos'] = tipoProductos
    context['stores'] = stores

    return render(request, 'store/products-brand.html', context)

#vista para API
class CustomResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        anterior = 0
        posterior = 0
        if self.page.has_previous():
            anterior = self.page.previous_page_number()

        if self.page.has_next():
            posterior = self.page.next_page_number()

        return Response({
            'next': posterior,
            'previous': anterior,
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'current': self.page.number,
            'limit': self.page_size,
            'results': data
        })

class ProductoAPIList(ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    pagination_class = CustomResultsSetPagination

    def get_queryset(self):
        producto_list = get_list_or_404(Product)
        return producto_list

class ProductFilterAPIList(ListAPIView):
    model = Product
    serializer_class = ProductSerializer
    pagination_class = CustomResultsSetPagination

    def get_queryset(self):
        category = self.kwargs["category"]
        logger.warn("Category : " + category)
        if category:
            queryset = Product.objects.filter(model__brand__typeProduct = category)
             
        brand = self.kwargs["brand"]
        logger.warn("Brand : " + brand)
        if brand:
            queryset = queryset.filter(model__brand = brand)
                
        return queryset

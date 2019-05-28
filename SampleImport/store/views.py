from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from .models import Product, Type, Brand, Store, Price
from datetime import date

# Create your views here.
def list_products(request):
    context = {}    
    tipoProductos = Type.objects.all()
    brands = Brand.objects.all()    
    context['tipoProductos'] = tipoProductos
    context['brands'] = brands
    
    products_list = Product.objects.all().order_by("name")
    paginator = Paginator(products_list,10)
    page = request.GET.get('page')

    products = paginator.get_page(page)
    context['products'] = products

    return render(request, 'store/store.html', context)

def detail_product(request,id):
    context = {}
    idProducto = id
    producto = get_object_or_404(Product, id = idProducto )
    prices = Price.objects.filter(product__id = idProducto, published_date = date.today())
    context['producto'] = producto
    if prices:
        context['prices'] = prices

    return render(request, 'store/product.html', context)
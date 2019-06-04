from django import template
from ..models import Price, Brand, Type

register = template.Library()

@register.inclusion_tag('store/prices.html')
def show_prices(idProd, idStore):
    precio = Price.objects.last_prices(idProd, idStore)
    return {'latest_price' : precio}

@register.inclusion_tag('store/brands.html',takes_context = True)
def show_brands(context, idType=None):
    if idType:
        brands = Brand.objects.filter(typeProduct__id = idType)
    else:
        brands = Brand.objects.all()
    return {'brands' : brands}

@register.inclusion_tag('store/types.html')
def show_type():
    types = Type.objects.all()
    return {'types' : types}
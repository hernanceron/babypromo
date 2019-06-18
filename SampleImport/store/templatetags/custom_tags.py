from django import template
from ..models import Price, Brand, Type
import logging

register = template.Library()
logger = logging.getLogger(__name__)

@register.inclusion_tag('store/tags/prices.html')
def show_prices(idProd, idStore):
    
    precio = Price.objects.last_prices(idProd, idStore)
    return {'latest_price' : precio}

@register.inclusion_tag('store/tags/brands.html',takes_context = True)
def show_brands(context, idType=None):
    if idType:
        brands = Brand.objects.filter(typeProduct__id = idType)
    else:
        brands = Brand.objects.all()
    return {'brands' : brands}

@register.inclusion_tag('store/tags/types.html')
def show_type():
    types = Type.objects.all()
    return {'types' : types}
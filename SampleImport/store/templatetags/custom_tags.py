from django import template
from ..models import Price

register = template.Library()

@register.inclusion_tag('store/prices.html')
def show_prices(idProd, idStore):
    precio = Price.objects.last_prices(idProd, idStore)
    return {'latest_price' : precio}
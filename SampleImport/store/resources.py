from import_export import resources
from .models import Type, Brand, Modelo, Size, Product, Price, Store

class TypeResource(resources.ModelResource):
    class Meta:
        model = Type

class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand

class ModeloResource(resources.ModelResource):
    class Meta:
        model = Modelo

class SizeResource(resources.ModelResource):
    class Meta:
        model = Size

class ProductoResource(resources.ModelResource):
    class Meta:
        model = Product

class PriceResource(resources.ModelResource):
    class Meta:
        model = Price
        import_id_fields = ('store','product','published_date','amount','discounted_price',)
        fields = ('store','product','published_date','amount','discounted_price',)

class StoreResource(resources.ModelResource):
    class Meta:
        model = Store
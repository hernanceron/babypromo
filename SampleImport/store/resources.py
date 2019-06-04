from import_export import resources, fields
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
    store = fields.Field(column_name="store", attribute="store")
    product = fields.Field(column_name="product", attribute="product")
    published_date = fields.Field(column_name="published_date",attribute="published_date")
    amount = fields.Field(column_name="amount",attribute="amount")
    discounted_price = fields.Field(column_name="discounted_price",attribute="discounted_price")

    class Meta:
        model = Price        
        skip_unchanged = True
        fields = ('id','store','product','published_date','amount','discounted_price',)

class StoreResource(resources.ModelResource):
    class Meta:
        model = Store
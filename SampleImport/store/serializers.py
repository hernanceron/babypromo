from rest_framework.serializers import ModelSerializer

from .models import Product, Modelo, Size, Brand, Type, Store, Price


class TipoSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"


class BrandSerializer(ModelSerializer):
    typeProduct = TipoSerializer()
    class Meta:
        model = Brand
        fields = "__all__"

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = "__all__"

class ModeloSerializer(ModelSerializer):
    brand = BrandSerializer()
    sizes = SizeSerializer(many=True)
    class Meta:
        model = Modelo
        fields = "__all__"



class ProductSerializer(ModelSerializer):
    model = ModeloSerializer()
    size = SizeSerializer()
    class Meta:
        model = Product
        fields = "__all__"


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = "__all__"
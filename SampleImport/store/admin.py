from __future__ import unicode_literals
from django.contrib import admin
from .models import Type, Brand, Modelo, Size, Product, Price, Store
from .resources import TypeResource, BrandResource, ModeloResource, SizeResource, ProductoResource, PriceResource, StoreResource
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class TypeAdmin(ImportExportModelAdmin):
    resource_class = TypeResource
admin.site.register(Type, TypeAdmin)

class BrandAdmin(ImportExportModelAdmin):
    resource_class = BrandResource
admin.site.register(Brand, BrandAdmin)

class ModeloAdmin(ImportExportModelAdmin):
    list_display = ('name','brand',)
    resource_class = ModeloResource
admin.site.register(Modelo, ModeloAdmin)

class SizeAdmin(ImportExportModelAdmin):
    resource_class = SizeResource
admin.site.register(Size, SizeAdmin)

class ProductoAdmin(ImportExportModelAdmin):
    resource_class = ProductoResource
admin.site.register(Product, ProductoAdmin)

class StoreAdmin(ImportExportModelAdmin):
    resource_class = StoreResource
admin.site.register(Store, StoreAdmin)

class PriceAdmin(ImportExportModelAdmin):
    resource_class = PriceResource
admin.site.register(Price, PriceAdmin)
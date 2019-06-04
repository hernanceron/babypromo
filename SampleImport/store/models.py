from __future__ import unicode_literals

from django.db import models

class PriceManager(models.Manager):
    def last_prices(self, idProd,idStore):        
        try:
            result = self.filter(product__id = idProd, store__id = idStore).latest('published_date')
        except Price.DoesNotExist:
            result = None
        return result

#TIPO DE PRODUCTO
class Type(models.Model):
    INACTIVO = 'INA'
    ACTIVO = 'ACT'
    STATUS = (
        ( INACTIVO, 'Inactivo'),
        ( ACTIVO, 'Activo'),
    )
    name = models.CharField(max_length = 60 , default = None)
    status = models.CharField(max_length = 3 ,
                                choices = STATUS,
                                default = ACTIVO,)

    def __str__(self):
        return '%s' % ( self.name)

#MARCA DE PRODUCTO
class Brand(models.Model):
    INACTIVO = 'INA'
    ACTIVO = 'ACT'
    STATUS = (
        ( INACTIVO, 'Inactivo'),
        ( ACTIVO, 'Activo'),
    )
    name = models.CharField(max_length = 20, default = None)
    status = models.CharField(max_length = 3 ,
                              choices = STATUS,
                              default = ACTIVO,)
    typeProduct = models.ForeignKey(Type, on_delete = models.CASCADE, default= 1)

    def __str__(self):
        return '%s' % (self.name)

#Size del producto
class Size(models.Model):
    INACTIVO = 'INA'
    ACTIVO = 'ACT'
    STATUS = (
        ( INACTIVO, 'Inactivo'),
        ( ACTIVO, 'Activo'),
    )
    name = models.CharField(max_length = 60 , default = None)
    status = models.CharField(max_length = 3 ,
                                choices = STATUS,
                                default = ACTIVO,)


    def __str__(self):
        return '%s' % ( self.name)


#MODELO DE PRODUCTO
class Modelo(models.Model):
    INACTIVO = 'INA'
    ACTIVO = 'ACT'
    STATUS = (
        ( INACTIVO, 'Inactivo'),
        ( ACTIVO, 'Activo'),
    )
    name = models.CharField(max_length = 60 , default = None)
    status = models.CharField(max_length = 3 ,
                                choices = STATUS,
                                default = ACTIVO,)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, default= None)
    sizes = models.ManyToManyField(Size)

    def __str__(self):
        return '%s' % ( self.name)

class Product(models.Model):
    name = models.CharField(max_length = 256, default = None)   #nombreProducto
    internalCode = models.CharField(max_length = 20, default = None) #codigo   
    quantity = models.IntegerField(default = 0) #quantity
    model = models.ForeignKey(Modelo, on_delete = models.CASCADE, default = None, blank=True, null=True) #Modelo
    size = models.ForeignKey(Size, on_delete = models.CASCADE, default = None, blank=True, null=True) #size        
    principalCode = models.CharField(max_length = 10, default = None)  #CodBaby  
    image_url = models.CharField(max_length = 256, default = None)     #web   
        
    def __str__(self):
        return '%s %s' % (self.principalCode, self.name)
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail_product', args=[str(self.id)])

class Store(models.Model):   
    INACTIVO = 'INA'
    ACTIVO = 'ACT'
    STATUS = (
        ( INACTIVO, 'Inactivo'),
        ( ACTIVO, 'Activo')
    )
    name = models.CharField(max_length = 20, default = None)
    status = models.CharField(max_length = 3 ,
                              choices = STATUS,
                              default = ACTIVO,)
    
    products = models.ManyToManyField(Product, through='Price')

    def __str__(self):
        return '%s' % (self.name)

class Price(models.Model):
    store = models.ForeignKey(Store, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    published_date = models.DateField()
    amount = models.CharField(max_length = 10)
    discounted_price = models.CharField(max_length = 10)
    objects = PriceManager()
    class Meta:
        ordering = ['published_date']

        def __unicode__(self):
            return self.amount

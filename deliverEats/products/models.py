from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Product(models.Model):
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        permissions = [
            ("product_buy", "Puede comprar un producto"),
            ("product_add_to_shopping_cart", "Puede agregar un producto al carrito"),
        ]

    name = models.CharField(u'Nombre', max_length=256)
    description = models.TextField(u"Descripción", null=True, blank=True)
    category = models.ManyToManyField('Category', verbose_name="Categorías")
    price = models.DecimalField(u"Precio", max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField(u"Stock", default=0)

    def __str__(self):
        return self.name


class ProductDetail(models.Model):
    class Meta:
        verbose_name = 'Detalle de producto'
        verbose_name_plural = 'Detalles de productos'

    product = models.ForeignKey("Product", verbose_name="Producto", on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(u"cantidad", validators=[MinValueValidator(1)])

    def __str__(self):
        return self.product.name

    @property
    def total(self):
        return self.product.price * self.quantity



class Category(models.Model):
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    name = models.CharField(u'Nombre', max_length=256)

    def __str__(self):
        return self.name


class Publicity(models.Model):
    class Meta:
        verbose_name = "Anuncio publicitario"
        verbose_name_plural = "Anuncios publicitarios"

    name = models.CharField(u'Nombre', max_length=256)
    description = models.TextField(u"Descripción", null=True, blank=True)
    image = models.ImageField(u"Imagen", upload_to='publicity_image', null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    image_file = models.ImageField(u"Imagen", upload_to='product_image')
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name="Producto")

    def __str__(self):
        return self.product.name
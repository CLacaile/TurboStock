from django.db import models
from .Product import Product
from .Aisle import Aisle

class Stock(models.Model):
    """
    This class models the association between an Aisle and a Product.
    """
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    aisle = models.ForeignKey(Aisle, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = (('product', 'aisle'))
    
    def __str__(self):
        return "Product: " + self.product.name + " at aisle " + self.aisle.name + " qty = " + self.quantity
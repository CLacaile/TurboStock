from django.db import models
from .Product import Product
from .Aisle import Aisle

class Stock(models.Model):
    """
    This class models the association between an Aisle and a Product.
    The PK is the ID but the tuple (product, aisle) is unique.
    
    Attributes:
        id (int): The ID of the record. It shouldn't have any use but it is the PK.
        product (int): The ID of the product. The tuple (product, aisle) is unique.
            It is a FK from the Product table.
        aisle (int): The ID of the aisle in which the product is. The tuple (product, 
        aisle) is unique. It is a FK from the Aisle table.
        quantity (int): The quantity of product in the aisle
    """
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    aisle = models.ForeignKey(Aisle, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    objects = models.Manager()


    class Meta:
        unique_together = (('product', 'aisle'))
    
    def __str__(self):
        return "Product: " + self.product.name + " at aisle " + self.aisle.name + " qty = " + self.quantity

    def save(self, *args, **kwargs):
        if self.quantity < 0:
            raise ValueError
        else:
            super().save(*args, **kwargs)

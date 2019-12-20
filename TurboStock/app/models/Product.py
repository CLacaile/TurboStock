from django.db import models

class Product(models.Model):
    """
    This class models a product that will be stored in one or more Aisles

    Attributes:
        id (int): the ID of the product. It is the PK of this class.
        name (char): the name of the product. The max length is 50 char.
        unit_price (float): the unit price of the product.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name
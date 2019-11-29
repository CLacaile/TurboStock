from django.db import models

class Product(models.Model):
    """
    This class models a product that will be stored in one or more Aisles
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name
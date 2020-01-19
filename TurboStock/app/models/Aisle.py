from django.db import models
from .Store import Store

class Aisle(models.Model):
    """
    This class models an Aisle in a store.

    Attributes:
        id (int): the ID of the aisle. It is the PK.
        name (str): the name of the aisle. It should represent a category of products.
            The max length is 50 char.
        store (int): the ID of the store in which the aisle is located. It is a FK from
        the table Store. When the store is deleted, the aisle is also deleted.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    objects = models.Manager()


    def __str__(self):
        return self.name
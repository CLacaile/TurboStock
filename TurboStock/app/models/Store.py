from django.db import models

class Store(models.Model):
    """
    This class models a store.

    Attributes:
        id (int): the ID of the store. It is the PK of the table.
        address (str): the address of the store. The max length is 100 char.
        city (str): the city of the store. The max length is 50 char.
    """
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=50, default="")
    #objects = models.Manager()


    def __str__(self):
        return "Store " + str(self.id) + " - " + self.city

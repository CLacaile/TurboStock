from django.db import models
from .Store import Store

class Aisle(models.Model):
    """
    This class models an Aisle in a store.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
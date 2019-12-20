from django.db import models

class Store(models.Model):
    """
    This class models a store
    """
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return "Store #" + self.id
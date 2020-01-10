from django.db import models
from .User import User
from .Aisle import Aisle

class AisleManager(User):
    """
    This class models an Aisle Manager of an aisle in a store.

    Attributes:
        aisle (int): the ID of the Aisle of which the manager is in charge. 
            It is a FK from Aisle.
    """
    aisle = models.OneToOneField(Aisle, null=True, on_delete=models.CASCADE)
from django.db import models
from .User import User
from .Aisle import Aisle

class AisleManager(User):
    """
    This class models an Aisle Manager of an aisle in a store
    """
    aisle = models.OneToOneField(Aisle, on_delete=models.CASCADE)
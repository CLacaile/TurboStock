from django.db import models
from .User import User
from .Store import Store

class StoreManager(User):
    """
    This class models a Store Manager of a store.

    Attributes:
        store (int): the id of the store that the manager handles. If the
            store is deleted, the field keeps the value.
    """
    store = models.OneToOneField(Store, null=True, on_delete=models.CASCADE)
    objects = models.Manager()


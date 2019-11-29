from django.db import models
from .User import User
from .Store import Store

class StoreManager(User):
    """
    This class models a Store Manager of a store
    """
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
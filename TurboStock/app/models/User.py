from django.db import models

from app.models import *


class User(models.Model):
    """
    This class is the base class for any user of the app. It should not be instanciated at any
    moment. Use CEO, AisleManager or StoreManager instead.

    Attributes:
        id (int): The ID of the user that is incremented automatically by Django.
            It is the PK.
        first_name (str): The first name of the user. This field has a maximum length of 50 char.
        last_name (str): The last name of the user. This field has a maximum length of 50 char.
        email (str): The email address of the user. This field has a maximum length of 100 char.
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    last_login = models.CharField(null=True, default=None, max_length=100)
    objects = models.Manager()

    def is_authenticated(self):
        return True

    def __str__(self):
        return self.first_name + " " + self.last_name

    child_class_names = (
        'AisleManager',
        'CEO',
        'StoreManager',
    )

    def child_object(self):
        for child_class_name in self.child_class_names:
            try:
                return self.__getattribute__(child_class_name.lower())
            except:
                pass
        return self

    def has_permission_on_item(self, item):
        user = self.child_object()
        user_class = type(user).__name__
        item_class = type(item).__name__

        # If user isCEO
        if user_class == CEO.__name__:
            return True

        # If user is StoreManager
        if user_class == StoreManager.__name__:
            # If item is Store
            if item_class == Store.__name__:
                if item.id == user.store_id:
                    return True
            # If item is Aisle
            if item_class == Aisle.__name__:
                if item.store_id == user.store_id:
                    return True
            return False

        # If user is AisleManager
        if user_class == AisleManager.__name__:
            # If item is Store
            if item_class == Store.__name__:
                return False
            # If item is Aisle
            if item_class == Aisle.__name__:
                if item.id == user.aisle_id:
                    return True
            return False

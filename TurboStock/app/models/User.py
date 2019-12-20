from django.db import models

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
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

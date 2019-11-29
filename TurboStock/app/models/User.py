from django.db import models

class User(models.Model):
    """
    This class is the base class for any user of the app
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
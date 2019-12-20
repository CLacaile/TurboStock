from django.db import models

class User(models.Model):
    """
    This class is the base class for any user of the app
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

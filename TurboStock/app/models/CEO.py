from django.db import models

from .User import User


class CEO(User):
    """
    This class models the CEO of the stores Sport+
    """
    objects = models.Manager()


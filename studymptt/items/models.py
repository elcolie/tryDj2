from django.db import models


class Item(models.Model):
    """
    Represent the product in the system. Because I start the coding from `Cart`
    Therefore I put it as an `item`.
    """
    name = models.CharField(max_length=255)

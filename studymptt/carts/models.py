from django.contrib.auth import get_user_model
from django.db import models

from items.models import Item

User = get_user_model()


class Cart(models.Model):
    """Let Cart be a meta. And order_items is reverse relation"""
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=5, default=0.085)
    tax_total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    # Use ORM here to help you get the count() of each item
    # 1 item represent 1 qty
    order_items = models.ManyToManyField(Item)

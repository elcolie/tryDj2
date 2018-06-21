from rest_framework import serializers

from carts.models import Cart


class CartSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()

    class Meta:
        model = Cart
        fields = [
            'created_by',
            'order_items',
            'subtotal',
            'tax_percentage',
            'tax_total',
            'total',
        ]


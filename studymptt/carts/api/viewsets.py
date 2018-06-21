from rest_framework import viewsets

from carts.api.serializers import CartSerializer
from carts.models import Cart


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from carts.api.serializers import CartSerializer
from carts.models import Cart


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

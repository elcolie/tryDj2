from django.contrib.auth import get_user_model
from django.test import TestCase
from model_mommy import mommy
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from carts.models import Cart
from items.models import Item

User = get_user_model()


class TestCart(TestCase):
    def setUp(self):
        pass

    def test_carts(self):
        john = mommy.make(User, username='John', email='john@example.com', password='john1234')
        client = APIClient()
        client.force_authenticate(user=john)
        mommy.make(Item, _quantity=5)
        url = reverse('api:cart-list')
        data = {
            'order_items': [item.id for item in Item.objects.all()],
            'subtotal': "0.00",
            'tax_percentage': "0.00",
            'tax_total': "0.00",
            'total': "0.00",
        }
        res = client.post(url, data=data, format='json')
        cart = Cart.objects.first()
        assert 1 == Cart.objects.count()
        assert 5 == cart.order_items.count()
        assert status.HTTP_201_CREATED == res.status_code

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from keydatecases.api.serializers import ICD10Serializer, KeyDateCaseSerializer
from keydatecases.models import ICD10, KeyDateCase


class CaseICD10Connection(APITestCase):
    def setUp(self):
        data1 = {
            'primary_key_number': "XS",
            'star_key_number': "XS",
            'additional_key_number': "XS",
            'preferred_short_description': "XS",
        }
        data2 = {
            'name': "Test",
        }
        self.data1 = data1
        self.data2 = data2

    def test_icd10_serializer(self):
        serializer = ICD10Serializer(data=self.data1)
        is_valid = serializer.is_valid()
        assert True is is_valid

    def test_keydatecase_serializer(self):
        serializer = KeyDateCaseSerializer(data=self.data2)
        is_valid = serializer.is_valid()
        assert True is is_valid

    def test_endpoint(self):
        data = {
            'case': self.data2,
            'icd_10': self.data1,
            'is_primary': True,
            'certainty': "S",
        }
        client = APIClient()
        url = reverse('api:case_icd10_connection-list')
        res = client.post(url, data=data, format='json')

        icd10 = ICD10.objects.first()
        c1 = icd10.connections.first()
        assert True is c1.is_primary
        assert 'S' == c1.certainty
        assert status.HTTP_201_CREATED == res.status_code
        assert 1 == ICD10.objects.count()
        assert 1 == KeyDateCase.objects.count()

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from contacts.api.serializers import ContactSerializer
from contacts.models import Contact


class ContactFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(field_name='email', lookup_expr='icontains', label='hello_email')
    subject = django_filters.CharFilter(lookup_expr='icontains')
    message = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'email',
            'subject',
            'message',
        ]


class ContactViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = ContactFilter
    search_fields = [
        'name',
        'email',
        'subject',
        'message',
    ]

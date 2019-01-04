import graphene
from graphene_django import DjangoObjectType

from contacts.models import Contact


class ContactType(DjangoObjectType):
    class Meta:
        model = Contact


class Query(graphene.ObjectType):
    contacts = graphene.List(ContactType)

    def resolve_contacts(self, info, **kwargs):
        """
        SELECT *
        FROM Contact_tbl
        :param info:
        :param kwargs:
        :return:
        """
        return Contact.objects.all()


schema = graphene.Schema(query=Query)

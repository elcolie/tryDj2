from django.forms import ModelForm

from contacts.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]

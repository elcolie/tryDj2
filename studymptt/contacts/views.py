from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status

from contacts.forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Good Form', status=status.HTTP_201_CREATED)
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

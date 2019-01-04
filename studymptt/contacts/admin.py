from django.contrib import admin

from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    __basic__ = [
        'name',
        'email',
        'subject',
        'message',
    ]
    list_display = __basic__
    list_display_links = __basic__


admin.site.register(Contact, ContactAdmin)

from django.contrib import admin

from pois.models import PointOfInterest


class PointOfInterestAdmin(admin.ModelAdmin):
    pass


admin.site.register(PointOfInterest, PointOfInterestAdmin)

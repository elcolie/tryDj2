from django.contrib import admin

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from genres.models import Genre

admin.site.register(Genre, MPTTModelAdmin)

from django.contrib import admin

from tweets.models import Tweet


class TweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'text']
    list_display_links = list_display


admin.site.register(Tweet, TweetAdmin)

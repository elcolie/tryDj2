from django.contrib import admin

from retweets.models import ReTweet


class ReTweetAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'tweet']
    list_display_links = list_display


admin.site.register(ReTweet, ReTweetAdmin)

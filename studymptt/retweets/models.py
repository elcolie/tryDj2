from django.db import models

from tweets.models import Tweet


class ReTweet(models.Model):
    text = models.CharField(max_length=100)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='re_tweets', related_query_name='re_tweet')

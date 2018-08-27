from actstream import action
from rest_framework import serializers

from retweets.models import ReTweet
from tweets.api.serializers import TweetSerializer


class ReTweetSerializer(serializers.ModelSerializer):
    tweet_detail = TweetSerializer(source='tweet', read_only=True)

    class Meta:
        model = ReTweet
        fields = [
            'id',
            'text',
            'tweet',
            'tweet_detail',
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        re_tweet = super().create(validated_data)
        action.send(user, verb='created re-tweet', action_object=re_tweet)
        return re_tweet

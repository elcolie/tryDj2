from actstream import action
from rest_framework import serializers

from tweets.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = [
            'id',
            'text',
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        tweet = super().create(validated_data)
        action.send(user, verb='created tweet', action_object=tweet)
        return tweet

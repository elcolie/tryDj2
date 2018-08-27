from actstream.models import Action
from django.contrib.auth import get_user_model
from generic_relations.relations import GenericRelatedField
from rest_framework import serializers

from retweets.api.serializers import ReTweetSerializer
from retweets.models import ReTweet
from tweets.api.serializers import TweetSerializer
from tweets.models import Tweet

User = get_user_model()


class PlainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]


class TimelineSerializer(serializers.ModelSerializer):
    __basic_fields = {
        Tweet: TweetSerializer(),
        ReTweet: ReTweetSerializer(),
        User: PlainUserSerializer(),
    }
    actor = GenericRelatedField(__basic_fields)
    # Can use only 1 `GenericRelatedField` per `serializer`
    action_object = GenericRelatedField(__basic_fields)
    target = GenericRelatedField(__basic_fields)

    class Meta:
        model = Action
        fields = [
            'id',
            'actor',
            'verb',
            'description',
            'target',
            'action_object',
            'timestamp',
        ]

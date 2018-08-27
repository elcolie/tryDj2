from actstream import action
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from retweets.models import ReTweet
from tweets.models import Tweet

User = get_user_model()


class TestTimeline(TestCase):
    def setUp(self):
        # 2 persons
        self.john = User.objects.create(username='john')
        self.smith = User.objects.create(username='smith')
        self.tweet1 = Tweet.objects.create(text='This is first one')
        self.tweet2 = Tweet.objects.create(text='This is 2nd')
        self.retweet1 = ReTweet.objects.create(text='Benz', tweet=self.tweet1)
        self.retweet2 = ReTweet.objects.create(text='BMW', tweet=self.tweet2)

        action.send(self.john, verb='created', action_object=self.tweet1, target=self.smith)
        action.send(self.smith, verb='created', action_object=self.tweet2, target=self.john)
        action.send(self.john, verb='retweeted', action_object=self.retweet1, target=self.smith)

    def test_actor(self):
        url = reverse('api:timeline-list')
        client = APIClient()
        client.force_authenticate(user=self.john)
        res = client.get(url)
        self.assertEqual(status.HTTP_200_OK, res.status_code)

from django.apps import AppConfig
from django.contrib.auth import get_user_model


class TimelinesConfig(AppConfig):
    name = 'timelines'

    def ready(self):
        from actstream import registry
        registry.register(get_user_model())

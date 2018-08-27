from actstream.models import Action
from rest_framework import viewsets

from timelines.api.serializers import TimelineSerializer


class TimelineListView(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = TimelineSerializer

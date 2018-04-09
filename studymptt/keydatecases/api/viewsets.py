from rest_framework import viewsets

from keydatecases.api.serializers import CaseICD10ConnectionSerializer
from keydatecases.models import CaseICD10Connection


class CaseICD10ConnectionViewSet(viewsets.ModelViewSet):
    permission_classes = ()
    queryset = CaseICD10Connection.objects.all()
    serializer_class = CaseICD10ConnectionSerializer

from rest_framework import routers

from keydatecases.api.viewsets import CaseICD10ConnectionViewSet

app_name = 'api'
router = routers.DefaultRouter()

router.register(r'case-icd10-connection', CaseICD10ConnectionViewSet, base_name='case_icd10_connection')

urlpatterns = router.urls

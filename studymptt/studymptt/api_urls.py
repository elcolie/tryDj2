from rest_framework import routers

from carts.api.viewsets import CartViewSet
from keydatecases.api.viewsets import CaseICD10ConnectionViewSet
from timelines.api.viewsets import TimelineListView

app_name = 'api'
router = routers.DefaultRouter()

router.register(r'case-icd10-connection', CaseICD10ConnectionViewSet, base_name='case_icd10_connection')
router.register(r'carts', CartViewSet, base_name='cart')
router.register(r'timelines', TimelineListView, base_name='timeline')

urlpatterns = router.urls

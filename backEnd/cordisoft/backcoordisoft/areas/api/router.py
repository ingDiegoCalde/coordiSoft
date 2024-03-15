from rest_framework.routers import DefaultRouter
from areas.api.views import AreaApiViewSet

router_areas = DefaultRouter()
router_areas.register(prefix='areas', basename='areas', viewset=AreaApiViewSet)


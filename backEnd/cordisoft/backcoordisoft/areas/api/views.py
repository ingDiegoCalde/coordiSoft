from rest_framework.viewsets import ModelViewSet
from areas.models import Area
from areas.api.serializers import AreaSerializer

class AreaApiViewSet(ModelViewSet):
    serializer_class = AreaSerializer
    queryset = Area.objects.all()

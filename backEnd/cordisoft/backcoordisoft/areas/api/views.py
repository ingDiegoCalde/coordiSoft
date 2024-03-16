from rest_framework.viewsets import ModelViewSet
from areas.models import Area
from areas.api.serializers import AreaSerializer
from areas.api.permissions import IsAdminReadOnly

class AreaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = AreaSerializer
    queryset = Area.objects.all()

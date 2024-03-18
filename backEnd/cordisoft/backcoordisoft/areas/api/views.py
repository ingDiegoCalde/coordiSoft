from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from areas.models import Area
from areas.api.serializers import AreaSerializer
from areas.api.permissions import IsAdminReadOnly

class AreaApiViewSet(ModelViewSet):
    permission_classes = [IsAdminReadOnly]
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
    #Vamos a filtrar y a devolver lo que tenga estado en True
    #queryset = Area.objects.filter(state=True)
    lookup_field = 'slug' #esto cambia el endpoint diciendo que ya no busque o elimine por ID si no que ahora sera por slug.
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state', 'name_area']
#Que datos vamos a trabajar de nuestra app
from rest_framework import serializers
from areas.models import Area

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['id', 'name_area', 'slug', 'state']

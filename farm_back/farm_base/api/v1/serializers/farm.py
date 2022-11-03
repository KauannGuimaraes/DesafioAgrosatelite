from django.contrib.gis.geos import GEOSGeometry
from osgeo import ogr
from rest_framework import serializers
from rest_framework_gis.fields import GeometryField


from farm_base.models import Farm

class FarmListSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(FarmListSerializer, self).__init__(*args, **kwargs)
        request = kwargs['context']['request']
        include_geometry = request.GET.get('include_geometry', "false")
        if include_geometry.lower() == "true":
            self.fields['geometry'] = GeometryField(read_only=True)

    class Meta:
        model = Farm
        fields = '__all__'
        read_only_fields = ['id', 'name', 'municipality', 'state', 'centroid', 'area', 'owner']


class FarmCreateSerializer(serializers.ModelSerializer):
    def validate_geometry(self, data):
        if data.hasz:
            g = ogr.CreateGeometryFromWkt(data.wkt)
            g.Set3D(False)
            data = GEOSGeometry(g.ExportToWkt())
        return data

    class Meta:
        model = Farm
        fields = ['id', 'name', 'municipality', 'state', 'centroid', 'area', 'owner']
        read_only_fields = ['id']


class FarmDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Farm
        fields = ['id', 'name', 'municipality', 'state', 'centroid', 'area', 'owner']
        read_only_fields = ['id', 'centroid', 'area']

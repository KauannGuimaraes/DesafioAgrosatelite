import logging
from requests import Response
from rest_framework import generics, viewsets

from farm_base.api.v1.serializers import FarmListSerializer, \
    FarmCreateSerializer, FarmDetailSerializer
from farm_base.models import Farm, Owner

class FarmListCreateView(generics.ListCreateAPIView):
    queryset = Farm.objects.filter(is_active=True)
    serializer_class = FarmListSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FarmListSerializer
        else:
            return FarmCreateSerializer

    def perform_create(self, serializer):
        farm = serializer.save()
        area = float(farm.geometry.area)
        centroid = farm.geometry.centroid
        serializer.save(area=area, centroid=centroid)


class FarmRetrieveUpdateDestroyView(
    generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.filter(is_active=True)
    serializer_class = FarmDetailSerializer

class FarmListName(generics.ListAPIView):
    serializer_class = FarmListSerializer
    def get_queryset(self):
        farmname = self.kwargs['name']
        farm = Farm.objects.filter(name = farmname)
        return farm

class FarmListMunicipality(generics.ListAPIView):
    serializer_class = FarmListSerializer
    def get_queryset(self):
        farmMunicipality = self.kwargs['municipality']
        farm = Farm.objects.filter(municipality = farmMunicipality)
        return farm

class FarmListState(generics.ListAPIView):
    serializer_class = FarmListSerializer
    def get_queryset(self):
        farmState = self.kwargs['state']
        farm = Farm.objects.filter(state = farmState)
        return farm

class FarmListOwnerName(generics.ListAPIView):
    serializer_class = FarmListSerializer
    def get_queryset(self):
        farmOwnerName = self.kwargs['name']
        farm = Farm.objects.filter(owner__name__contains=farmOwnerName)
        return farm

class FarmListOwnerDocument(generics.ListAPIView):
    serializer_class = FarmListSerializer
    def get_queryset(self):
        farmOwnerDocument = self.kwargs['document']
        farm = Farm.objects.filter(owner__document__contains=farmOwnerDocument)
        return farm
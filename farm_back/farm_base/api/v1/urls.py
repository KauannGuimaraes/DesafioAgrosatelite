from __future__ import unicode_literals
from django.urls import path, re_path
from django.conf.urls import url

from farm_base.api.v1.views.farm import FarmListName, FarmListMunicipality, FarmListState, FarmListOwnerName, FarmListOwnerDocument
from .views import FarmListCreateView, \
    FarmRetrieveUpdateDestroyView, OwnerListCreateView, \
    OwnerRetrieveUpdateDestroyView

urlpatterns = [
    path('farms', FarmListCreateView.as_view(),
         name="farms-list-create"),
    path('farms/<int:pk>', FarmRetrieveUpdateDestroyView.as_view(),
         name="farms-retrieve-update-destroy"),
    path('farms/name/<str:name>', FarmListName.as_view(),
         name="farm-name"),
    path('farms/municipality/<str:municipality>', FarmListMunicipality.as_view(),
         name="farm-Municipality"),
    path('farms/State/<str:state>', FarmListState.as_view(),
         name="farm-State"),
    path('farms/owners/<str:name>', FarmListOwnerName.as_view(),
         name="farm-Owner-Name"),
    path('farms/ownerdoc/<int:document>', FarmListOwnerDocument.as_view(),
         name="farm-Owner-Document"),

    path('owners', OwnerListCreateView.as_view(),
         name="owners-list-create"),
    path('owners/<int:pk>',
         OwnerRetrieveUpdateDestroyView.as_view(),
         name="owners-retrieve-update-destroy"),
     

]

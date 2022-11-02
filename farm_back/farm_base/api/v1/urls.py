from __future__ import unicode_literals
from django.urls import path

from farm_base.api.v1.views.farm import FarmListName, FarmListMunicipality, FarmListState, FarmListOwnerName
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
    path('farms/Municipality/<str:Municipality>', FarmListMunicipality.as_view(),
         name="farm-Municipality"),
    path('farms/State/<str:State>', FarmListState.as_view(),
         name="farm-State"),
    path('farms/Owners/<str:Owner>', FarmListOwnerName.as_view(),
         name="farm-Owner-Name"),

    path('owners', OwnerListCreateView.as_view(),
         name="owners-list-create"),
    path('owners/<int:pk>',
         OwnerRetrieveUpdateDestroyView.as_view(),
         name="owners-retrieve-update-destroy"),
     

]

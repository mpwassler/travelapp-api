
from django.urls import path
from django.conf.urls import url, include

from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register(r'trips', views.TripViewset)

trips_router = routers.NestedDefaultRouter(router, r'trips', lookup='trips')
trips_router.register(r'places', views.PlaceViewset)

router.register(r'users', views.UserViewset)

urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^', include(trips_router.urls)),
)
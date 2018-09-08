from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('viajes', views.ViajeRUD)

urlpatterns = [
    url('viaje', include(router.urls))
]
from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('viajes', views.ViajeRUD)
router.register('noticias', views.NoticiaViajeRUD)

urlpatterns = [
    url('', include(router.urls)),
    url('noticia/(?P<viaje>.+)/', include(router.urls))
]
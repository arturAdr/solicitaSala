from django.conf.urls import url, include
from rest_framework import routers
from sala import views as views_sala
from agenda import views as views_agenda

router = routers.DefaultRouter()
router.register(r'salas', views_sala.SalaViewSet)
router.register(r'agendas', views_agenda.AgendaViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
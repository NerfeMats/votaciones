
from django.urls import path
from .views import AltaPartido, Presentacion, Votar, Resultados, ListarPartidosPoliticos, UrnaView, BotonVotar


urlpatterns = [
    
 path("", Presentacion.as_view(), name="presentacion"),
 path("altapartido/", AltaPartido.as_view(), name="altapartido"),   
 path("votar/", Votar.as_view(), name="votar"),
 path("resultados/", Resultados.as_view(), name="resultados"),
 path("listarpartidos/", ListarPartidosPoliticos.as_view(), name="listarpartidos"),
 path('urna/', UrnaView.as_view(), name='urna'),
 path('botonvotar/<pk>/', BotonVotar.as_view(), name='botonvotar')
]

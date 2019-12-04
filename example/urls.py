from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from example import views
#>;v
urlpatterns = [
     #trae solo la tabla de autobus
     re_path(r'^lista_autobuses/$', views.AutobusList.as_view() ),
     re_path(r'^detalle_autobus/(?P<id>\d+)$', views.AutobusDetail.as_view() ),
     #actualiza status de autobus
     re_path(r'^update_status/(?P<id>\d+)$', views.UdapteStatus.as_view() ),
     #Trae metodos de pagos y puede insertar uno nuevo
     re_path(r'^lista_pago/$', views.PagoList.as_view() ),
     #trae las clases y se puede ingresar uno nuevo
     re_path(r'^lista_clase/$', views.ClaseList.as_view() ),
     #trae ciudades y colocar nuevo
     re_path(r'^lista_ciudad/$', views.CiudadList.as_view() ),
     #trae rutas con el nombre de las ciudad destino, no introducir costo es automatico
     re_path(r'^lista_ruta/$', views.RutaList.as_view() ),
     #trae los autobuses junto con el nombre de las llaves foraneas
     re_path(r'^lista_allautobus/$', views.AutobusAllList.as_view() ),
     #trae los asiento ingresar nuevo
     re_path(r'^lista_asiento/(?P<id>\d+)$', views.AsientoList.as_view() ),
     #actualizar con put el estado del asiento
     re_path(r'^detalle_asiento/$', views.AsientoDetail.as_view() ),
     #trae todos los boletos junto a los nombres de las llaves foraneas
     re_path(r'^lista_boletos/$', views.BoletoList.as_view() ),
     #actualizar algun balor de boleto o traer 1 boleto
     re_path(r'^detalle_boletos/(?P<id>\d+)$', views.BoletoDetail.as_view() ),

]
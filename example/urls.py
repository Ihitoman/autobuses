from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from example import views

urlpatterns = [

     re_path(r'^lista_autobuses/$', views.AutobusList.as_view() ),
     re_path(r'^detalle_autobus/(?P<id>\d+)$', views.AutobusDetail.as_view() ),
     re_path(r'^update_tipo/(?P<id>\d+)$', views.UdapteTipo.as_view() ),
     re_path(r'^update_status/(?P<id>\d+)$', views.UdapteStatus.as_view() ),
     
]
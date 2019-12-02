from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404

from example.models import MetodoPago
from example.models import ClaseAutobus
from example.models import Ciudad
from example.models import Ruta
from example.models import Autobus
from example.models import asiento
from example.models import Boleto

from example.serializer import MetodoPagoSerializer
from example.serializer import ClaseAutobusSerializer
from example.serializer import CiudadSerializer
from example.serializer import RutaSerializer
from example.serializer import AutobusSelializer
from example.serializer import AutobusAllSelializer
from example.serializer import AsientoSerializer
from example.serializer import BoletoSerializer
from example.serializer import RutaAllSerializer
from example.serializer import BoletoAllSerializer

#vistas de extra
class AutobusList(APIView):
    
    def get(self, request, format=None):
        queryset = Autobus.objects.filter(delete=False)
        serializer = AutobusSelializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AutobusSelializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AutobusDetail(APIView):
    def get_object(self, id):
        try:
            return Autobus.objects.get(pk=id, delete=False)
        except Autobus.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = Autobus(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Autobus.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = Autobus(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UdapteStatus(APIView):
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            autobuss = Autobus.objects.get(pk=id)
            autobuss.status = request.data['status']
            autobuss.save()
            return Response('Guardado')


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

class PagoList(APIView):
    
    def get(self, request, format=None):
        queryset = MetodoPago.objects.filter(delete=False)
        serializer = MetodoPagoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MetodoPagoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#/////////////////////////////////////////////////////////////////////////////////////////////

class ClaseList(APIView):
    
    def get(self, request, format=None):
        queryset = ClaseAutobus.objects.filter(delete=False)
        serializer = ClaseAutobusSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ClaseAutobusSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#//////////////////////////////////////////////////////////////////////////////////////////

class CiudadList(APIView):
    
    def get(self, request, format=None):
        queryset = Ciudad.objects.filter(delete=False)
        serializer = CiudadSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CiudadSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#///////////////////////////////////////////////////////////////////////////

class RutaList(APIView):
    
    def get(self, request, format=None):
        queryset = Ruta.objects.filter(delete=False)
        serializer = RutaAllSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        postruta= Ruta.objects.create(
            ciudad_destino_id = request.data['ciudad_destino_id'],
            distancia = request.data['distancia'],
            costo = request.data['distancia'],
            hora_salida = request.data['hora_salida']
        )
        postruta.save()
        return Response(postruta.id)

#////////////////////////////////////////////////////////////////

class AutobusAllList(APIView):
    
    def get(self, request, format=None):
        queryset = Autobus.objects.filter(delete=False)
        serializer = AutobusAllSelializer(queryset, many=True)
        return Response(serializer.data)
    
#///////////////////////////////////////////////////////////////

class AsientoList(APIView):
    
    def get(self, request, format=None):
        queryset = asiento.objects.filter(delete=False)
        serializer = AsientoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = AsientoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class AsientoDetail(APIView):
    def get_object(self, id):
        try:
            return asiento.objects.get(pk=id, delete=False)
        except asiento.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = AsientoSerializer(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        asiento.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            autobuss = asiento.objects.get(pk=id)
            autobuss.status = request.data['status']
            autobuss.save()
            return Response('Guardado')

#//////////////////////////////////////////////////////////////////
class BoletoList(APIView):
    
    def get(self, request, format=None):
        queryset = Boleto.objects.filter(delete=False)
        serializer = BoletoAllSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BoletoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class BoletoDetail(APIView):
    def get_object(self, id):
        try:
            return Boleto.objects.get(pk=id, delete=False)
        except Boleto.DoesNotExist:
            return False
    
    def get(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = Boleto(example)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Boleto.objects.get(pk=id).delete()
        return Response("ok")
    
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            serializer = Boleto(example, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
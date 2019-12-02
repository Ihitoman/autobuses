from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import status


from django.shortcuts import get_object_or_404
from django.http import Http404

from example.models import Autobus

from example.serializer import AutobusSelializer

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

class UdapteTipo(APIView):
    def put(self, request, id, format=None):
        example = self.get_object(id)
        if example != False:
            autobuss = Autobus.objects.get(pk=id)
            autobuss.tipo = request.data['tipo']
            autobuss.save()
            return Response('Guardado')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////


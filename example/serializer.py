from rest_framework import routers, serializers

from example.models import MetodoPago
from example.models import ClaseAutobus
from example.models import Ciudad
from example.models import Ruta
from example.models import Autobus
from example.models import asiento
from example.models import Boleto

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = ('__all__')

class ClaseAutobusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaseAutobus
        fields = ('__all__')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__')

class RutaAllSerializer(serializers.ModelSerializer):
    ciudad_destino = serializers.ReadOnlyField(source='ciudad_destino_id.nombre')
    class Meta:
        model = Ruta
        fields = ('__all__')

class RutaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = ('__all__')

class AutobusSelializer(serializers.ModelSerializer):
    class Meta:
        model = Autobus
        fields = ('__all__')

class AutobusAllSelializer(serializers.ModelSerializer):
    ciudad_destino = serializers.ReadOnlyField(source='ruta_id.ciudad_destino_id.nombre')
    distancia = serializers.ReadOnlyField(source='ruta_id.distancia')
    hora_salida = serializers.ReadOnlyField(source='ruta_id.hora_salida')
    class Meta:
        model = Autobus
        fields = ('__all__')

class AsientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = asiento
        fields = ('__all__')

class BoletoAllSerializer(serializers.ModelSerializer):
    clase = serializers.ReadOnlyField(source='clase_id.nombre')
    metodo_pago = serializers.ReadOnlyField(source='metodopago_id.nombre')

    class Meta:
        model = Boleto 
        fields = ('__all__')

class BoletoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleto 
        fields = ('__all__')
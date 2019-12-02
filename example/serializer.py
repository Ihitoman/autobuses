from rest_framework import routers, serializers

from example.models import Autobus



class AutobusSelializer(serializers.ModelSerializer):
    class Meta:
        model = Autobus
        fields = ('__all__')


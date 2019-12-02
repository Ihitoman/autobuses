from django.db import models

# Create your views here.

class Autobus(models.Model):
    status = models.CharField(max_length=30, null=False)
    distanciaRuta = models.IntegerField( null=False )
    asientos = models.IntegerField( null=False )
    ruta = models.CharField(max_length=30, null=False)
    tipo = models.CharField(max_length=30, null=False)

    class Meta:
        db_table = "autobuses"


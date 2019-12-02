from django.db import models

# Create your views here.

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = "metodos_pagos"

class ClaseAutobus(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    precio = models.FloatField(null=False)

    class Meta:
        db_table = "clases_autobus"

class Ciudad(models.Model):
    nombre = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = "ciudades"

class Ruta(models.Model):
    #ciudad_origen_id = models.ForeignKey(Ciudad, on_delete=models.SET(-1))
    ciudad_destino_id = models.ForeignKey(Ciudad, on_delete=models.SET(-1))
    distancia = models.FloatField(null=False)
    costo = models.FloatField(null=False)
    hora_salida = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = "rutas"

class Autobus(models.Model):
    status = models.CharField(max_length=30, null=False)
    asientos = models.CharField(max_length=3, null=False )
    ruta = models.ForeignKey(Ruta, on_delete=models.SET(-1))
    clase = models.ForeignKey(ClaseAutobus, on_delete=models.SET(-1))

    class Meta:
        db_table = "autobuses"

class asiento(models.Model):
    autobus_id = models.ForeignKey(Autobus, on_delete=models.SET(-1))
    status = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = "asientos"

class Boleto(models.Model):
    clase_id = models.ForeignKey(ClaseAutobus, on_delete=models.SET(-1))
    descuento = models.FloatField(null=False)
    nombre_cleiente = models.CharField(max_length=50, null=False)
    correo = models.CharField(max_length=30, null = False)
    metodopago_id = models.ForeignKey(MetodoPago, on_delete=models.SET(-1))
    asiento = models.CharField(max_length=3, null=False)
    total = models.FloatField(null=False)
    autobus_id = models.ForeignKey(Autobus, on_delete=models.SET(-1))

    class Meta:
        db_table = "boletos"
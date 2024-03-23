from django.db import models

# Create your models here.


class Hospedaje(models.Model):
    id_hospedaje = models.AutoField(primary_key=True)
    nombre_hospedaje = models.CharField()
    direccion = models.CharField()
    calificacion = models.IntegerField()
    disponible = models.IntegerField(blank=True, null=True)
    id_propietaria = models.IntegerField(blank=True, null=True)
    capacidades = models.TextField()  # This field type is a guess.
    nombre_imagen = models.CharField()
    precio_noche = models.IntegerField()


def __str__(self):
    return self.name
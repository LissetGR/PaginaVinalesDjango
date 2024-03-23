from rest_framework import serializers
from .models import Hospedaje

class hospedajeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Hospedaje
        fields= ('id_hospedaje', 'direccion', 'nombre_hospedaje','calificacion','capacidades', 'disponible', 'id_propietaria','precio_noche','nombre_imagen')
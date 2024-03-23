from rest_framework import generics
from .serializer import hospedajeSerializer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Hospedaje

# Create your views here.

def devolverHospedajes(request):
    queryset=Hospedaje.objects.all()
    serializer_class= hospedajeSerializer(queryset, many=True)
    return JsonResponse(serializer_class.data,safe=False)

# class devolverHospedajes(generics.ListCreateAPIView):
#     queryset=Hospedaje.objects.all()
#     serializer_class= hospedajeSerializer
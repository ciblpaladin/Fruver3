from typing import Any
from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import HttpResponse, JsonResponse
import json


class ListaTareas(generics.ListCreateAPIView):
  def __init__(self) -> None:
     pass

  def get(self, request):
    con : conexion = conexion()
    products = con.ejecutar_sp_y_guardar_resultados() 
     
    return JsonResponse(products, safe=False)


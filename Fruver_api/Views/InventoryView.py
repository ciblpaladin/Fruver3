from typing import Any
from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import HttpResponse, JsonResponse
import json


class ListaTareas(generics.ListAPIView):
  def __init__(self) -> None:
     pass

  def get(self, request):
    con : conexion = conexion()
    products = con.execute_reader("SP_getProducts()") 
     
    return JsonResponse(products, safe=False)


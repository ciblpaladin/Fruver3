from typing import Any
from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import HttpResponse

class ListaTareas(generics.ListCreateAPIView):
  def __init__(self) -> None:
     pass

  def get(self, request):
    con : conexion = conexion()
    con.ejecutar_sp_y_guardar_resultados() 
     
    
    return HttpResponse("Esto es una respuesta de la solicitud GET")


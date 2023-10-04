from typing import Any
from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import HttpResponse, JsonResponse
from ..DB.Repository.BoxInventaryRepos import BoxInventaryRepos

class Inventory:
  con = conexion()
  repos: BoxInventaryRepos = BoxInventaryRepos(con)

  class InvetoryBoxList(generics.ListAPIView):

    def get(self, request):
      
      inventory_box = Inventory.repos.get_all("SP_getBoxInventary()") 
      
      return JsonResponse(inventory_box, safe=False)

  class InvetoryUnitList(generics.ListAPIView):

    def get(self, request):
      
      inventory_unit = Inventory.repos.get_all("sp_get_box_inventary_unit()") 
      
      print(inventory_unit)
      return JsonResponse(inventory_unit.to_dict())  



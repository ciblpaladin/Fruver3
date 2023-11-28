from typing import Any
from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import HttpResponse, JsonResponse
from ..DB.Repository.BoxInventaryRepos import BoxInventaryRepos
from ..DB.Repository.InventoryRepos import InventoryRepos

class Inventory:
  con = conexion()
  repos: BoxInventaryRepos = BoxInventaryRepos(con)
  repos_in : InventoryRepos = InventoryRepos(con)

  class InvetoryBoxList(generics.ListAPIView):

    def get(self, request):
      
      inventory_box = Inventory.repos_in.filter(request,"sp_get_box_inventory") 
      
      return JsonResponse(inventory_box.to_dict(), safe=False)
    
    def post(self, request):

      data = Inventory.repos_in.create_inventory(request, "sp_set_box_inventary")
      return JsonResponse(data.to_dict(), safe=False)
  class InventoryBoxListDate(generics.ListAPIView):

      def post(self, request):

        data = Inventory.repos_in.filter(request, "sp_get_box_inventory")
        return JsonResponse(data.to_dict(), safe=False)
    
  class InvetoryUnitList(generics.ListAPIView):

    def get(self, request):
      
      inventory_unit = Inventory.repos.get_all("sp_get_box_inventary_unit()") 
      
      print(inventory_unit)
      return JsonResponse(inventory_unit.to_dict())  

    def post(self, request):

        data_entry = Inventory.repos.create(request, "sp_set_box_inventary_unit")
        return JsonResponse(data_entry.to_dict())

  class InventoryDateCheckView(generics.ListAPIView):

      def post(self, request):
        
        data_entry = Inventory.repos_in.filter(request, "sp_get_box_inventary_date")
        return JsonResponse(data_entry.to_dict())
      
  class InventoryUpdateView(generics.UpdateAPIView):
     
     def post(self, request):
        
        data_entry = Inventory.repos_in.create_inventory(request, "sp_update_box_inventary")
        return JsonResponse(data_entry.to_dict())
from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import JsonResponse
from ..DB.Repository.SuppliersRepos import SuppliersRepos

class Suppliers:

    con = conexion()
    repos: SuppliersRepos = SuppliersRepos(con)
        
    class SuppliersViewList(generics.ListAPIView):

        
        def get(self, request):
            
            data = Suppliers.repos.get_all("SP_getSuppliers()")
            return JsonResponse(data.to_dict())

        def post(self, request):

            data_entry = Suppliers.repos.create(request, "sp_set_suppliers")
            return JsonResponse(data_entry.to_dict())

class SuppliersDebts:

    con = conexion()
    repos: SuppliersRepos = SuppliersRepos(con)
        
    class SuppliersDebtsViewList(generics.ListAPIView):

        
        def get(self, request):
            
            data = SuppliersDebts.repos.get_all("sp_get_suppliers_debts()")
            return JsonResponse(data.to_dict())
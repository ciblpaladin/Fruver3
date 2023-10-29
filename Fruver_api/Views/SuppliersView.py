from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import JsonResponse
from ..DB.Repository.SuppliersRepos import SuppliersRepos

class Suppliers:

    con = conexion()
    repos: SuppliersRepos = SuppliersRepos(con)
        
    class SuppliersViewList(generics.ListAPIView):

        
        def get(self, request):
            
            data = Suppliers.repos.get_all("sp_get_suppliers()")
            return JsonResponse(data.to_dict())

        def post(self, request):

            data_entry = Suppliers.repos.create(request, "sp_set_suppliers")
            return JsonResponse(data_entry.to_dict())
    
    class SuppliersFilterView(generics.ListAPIView):

        def post(self, request):

            data_entry = Suppliers.repos.filter(request, "sp_filter_suppliers")
            return JsonResponse(data_entry.to_dict())
        
    class SuppliersUpdateView(generics.UpdateAPIView):

            def post(self, request):

                supplier_update = Suppliers.repos.create(request, "sp_update_suppliers")
                return JsonResponse(supplier_update.to_dict())

class SuppliersDebts:

    con = conexion()
    repos: SuppliersRepos = SuppliersRepos(con)
        
    class SuppliersDebtsViewList(generics.ListAPIView):

        
        def get(self, request):
            
            data = SuppliersDebts.repos.get_all("sp_get_suppliers_debts()")
            return JsonResponse(data.to_dict())
        
        def post(self, request):

            data_entry = SuppliersDebts.repos.create(request, "sp_set_suppliers_debts")
            return JsonResponse(data_entry.to_dict())

    class SuppliersDebtsFilterView(generics.ListAPIView):

        def post(self, request):

            suppliers_debts_filter = Suppliers.repos.filter(request, "sp_filter_suppliers_debts")
            return JsonResponse(suppliers_debts_filter.to_dict())
        
    class SuppliersDebtsPayView(generics.UpdateAPIView):

        def post(self, request):

            suppliers_debts_pay = Suppliers.repos.filter(request, "sp_pay_off_suppliers_debt")
            return JsonResponse(suppliers_debts_pay.to_dict())

    class SuppliersDebtsPassView(generics.UpdateAPIView):

        def post(self, request):

            suppliers_debts_pay = Suppliers.repos.filter(request, "sp_settle_debt")
            return JsonResponse(suppliers_debts_pay.to_dict())             
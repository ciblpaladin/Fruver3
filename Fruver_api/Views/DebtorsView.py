from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import JsonResponse
from ..DB.Repository.DebtorsRepos import DebtorsRepos

class Debtors:

    con = conexion()
    repos: DebtorsRepos = DebtorsRepos(con)
        
    class DebtorsViewList(generics.ListAPIView):

        
        def get(self, request):
            
            data = Debtors.repos.get_all("SP_getDebtors()")
            return JsonResponse(data.to_dict())
        
        def post(self, request):

            data_entry = Debtors.repos.create(request, "sp_set_debtors")
            return JsonResponse(data_entry.to_dict())


class DebtorsCredits:

    con = conexion()
    repos: DebtorsRepos = DebtorsRepos(con)
        
    class DebtorsCreditsViewList(generics.ListAPIView):

        
        def get(self, request):
            
            data = DebtorsCredits.repos.get_all("sp_getdebors_credit()")
            return JsonResponse(data.to_dict())
        
        def post(self, request):

            data_entry = DebtorsCredits.repos.create(request, "sp_set_debtors_credit")
            return JsonResponse(data_entry.to_dict())
        
    class DebtorsCreditsViewEdit(generics.UpdateAPIView):

        def post(self, request):

            data_entry = DebtorsCredits.repos.create(request, "sp_edit_debtors_credit")
            return JsonResponse(data_entry.to_dict())
    
    class DebtorsCreditsViewFilter(generics.ListAPIView):

        def post(self, request):

            credit_filter = DebtorsCredits.repos.filter(request, "sp_filter_debtors_credit")
            return JsonResponse(credit_filter.to_dict())
        
    class CreditHistoryView(generics.ListAPIView):

        def get(self, request):
            
            history = DebtorsCredits.repos.get_all("sp_get_credit_history()")
            return JsonResponse(history.to_dict())

    class CreditPaysView(generics.ListAPIView):

        def get(self):

            pays = DebtorsCredits.repos.get_all("sp_get_debtors_credit_pays()")
            return JsonResponse(pays.to_dict())    
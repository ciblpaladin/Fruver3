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
            return JsonResponse(data, safe=False)


class DebtorsCredits:

    con = conexion()
    repos: DebtorsRepos = DebtorsRepos(con)
        
    class DebtorsCreditsViewList(generics.ListAPIView):

        
        def get(self, request):
            
            data = DebtorsCredits.repos.get_all("sp_getdebors_credit()")
            return JsonResponse(data, safe=False)
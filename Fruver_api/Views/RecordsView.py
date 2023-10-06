from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import JsonResponse
from ..DB.Repository.RecordRepos import RecordsRepos


class Records:

    con = conexion()
    repos: RecordsRepos = RecordsRepos(con)
        
    class RecordsViewList(generics.ListAPIView):

        def post(self, request):

            data_entry = Records.repos.delete(request, "sp_delete_soft_record")
            return JsonResponse(data_entry.to_dict())
    
    class RecordsFilterView(generics.ListAPIView):

        def post(self, request):
            data_entry = Records.repos.filter(request, 'sp_filter_table')
            return JsonResponse(data_entry.to_dict())
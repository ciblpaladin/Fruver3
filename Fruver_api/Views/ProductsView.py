from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import JsonResponse
from ..DB.Repository.ProductRepos import ProductRepos


class Products:

    con = conexion()
    repos: ProductRepos = ProductRepos(con)
        
    class ProductViewList(generics.ListAPIView):

        
        def get(self, request):
            
            data = Products.repos.get_all("SP_getProducts()")
            return JsonResponse(data, safe=False)

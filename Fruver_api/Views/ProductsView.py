from typing import Any
from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import HttpResponse, JsonResponse
from ..DB.Repository.ProductRepos import ProductRepos
import json


class Products:

    con = conexion()
    repos: ProductRepos = ProductRepos(con)
        
    class ProductViewList(generics.ListAPIView):

        def get(self, request):
            
            data = Products.repos.get_products()
            return JsonResponse(data, safe=False)

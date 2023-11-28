from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import JsonResponse
from ..DB.Repository.ProductRepos import ProductRepos


class Products:

    con = conexion()
    repos: ProductRepos = ProductRepos(con)
        
    class ProductViewList(generics.ListAPIView):

        
        def get(self, request):
            
            data = Products.repos.get_all("sp_get_products()")
            return JsonResponse(data.to_dict())

        def post(self, request):

            data_entry = Products.repos.create(request, "sp_set_products")
            return JsonResponse(data_entry.to_dict())
    
    class ProductCreateList(generics.CreateAPIView):

        
        def post(self, request):
            
            data = Products.repos.create(request,"sp_update_products")
            return JsonResponse(data.to_dict())
    class ProductfilterView(generics.ListAPIView):

        
        def post(self, request):
            
            data = Products.repos.filter(request,"sp_filter_product")
            return JsonResponse(data.to_dict())


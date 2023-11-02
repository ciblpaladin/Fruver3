from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import JsonResponse
from ..DB.Repository.UserRepos import UserRepos


class User:

    con = conexion()
    repos: UserRepos = UserRepos(con)
        
    class UserViewList(generics.ListAPIView):

        pass
        # def get(self, request):
            
        #     data = Products.repos.get_all("SP_getProducts()")
        #     return JsonResponse(data.to_dict())

        # def post(self, request):

        #     data_entry = Products.repos.create(request, "sp_set_products")
        #     return JsonResponse(data_entry.to_dict())

    class UserCreateList(generics.CreateAPIView):

        def post(self, request):

            user_create = User.repos.create_user(request, "sp_add_user")
            return JsonResponse(user_create.to_dict())
        
    class UserGetCredentialView(generics.ListAPIView):

        def post(self, request):

            user_details = User.repos.validate_login(request, "sp_get_user_byidcard")
            return JsonResponse(user_details.to_dict())
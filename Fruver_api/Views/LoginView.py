from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import JsonResponse
from ..DB.Repository.UserRepos import UserRepos


class Login:

    con = conexion()
    repos: UserRepos = UserRepos(con)
        
    class UserLoginView(generics.ListAPIView):

        pass
        # def get(self, request):
            
        #     data = Products.repos.get_all("SP_getProducts()")
        #     return JsonResponse(data.to_dict())

        def post(self, request):

            data_entry = Login.repos.authenticate_user(request)
            return data_entry
    class UserLogoutView(generics.ListAPIView):

        def post(self, request):

            data_entry = Login.repos.logout_view(request)
            return data_entry
        
    class UserCreateList(generics.CreateAPIView):

        def post(self, request):

            user_create = Login.repos.create_user(request, "sp_add_user")
            return JsonResponse(user_create.to_dict())
    
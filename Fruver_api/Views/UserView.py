from rest_framework import generics
from Fruver_api.DB.Conexion import conexion
from django.http import JsonResponse
from ..DB.Repository.UserRepos import UserRepos
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User as Auth_user
from ..Response_server.Response import Response
class User:

    con = conexion()
    repos: UserRepos = UserRepos(con)
        
    class UserCreateList(generics.CreateAPIView):

        def post(self, request):

            user_name = request.data["username"]
            password = request.data["password"]
            try :

                user = Auth_user.objects.create(username=user_name, password= password)

            except Exception as e:

                return Response(
                Status=True,
                Messague=f"Error al crear usuario {e} ",
                Data= []
            )
            # Generar un token para el usuario
            token, created = Token.objects.get_or_create(user=user)

            res = Response(
                Status=True,
                Messague="Usuario creado correctamente",
                Data= []
            )

            return JsonResponse(res.to_dict())
         
            
    
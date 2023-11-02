from .RepositoryABC import RepositoryABC
from ..Conexion import conexion
from ..ABC.AbsAlterTables import AbsAlterTables
from ...Security.password import Password
from ...Response_server.Response import Response
from ...Models.Box_inventary import UserAuth
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

class UserRepos(RepositoryABC, AbsAlterTables):

    def __init__(self, conn : conexion) -> None:
        super().__init__(conn=conn)

    def authenticate_user(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,  username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(
                Status=True,
                Messague= "Inicio de sesion exitoso.",
                Data=[]
            )
        else:
            return Response(
                Status=False,
                Messague= "Usuario o contraseña incorrecto",
                Data=[]
            )

    def logout_view(request):
        
        if request.user.is_authenticated:
            logout(request)
            return JsonResponse({'message': 'Logged out successfully.'})
        else:
            return JsonResponse({'message': 'User is not authenticated.'}, status=401)
    def validate_login(self,request,sp_name):
       
       login = self.create(request=request, sp_name=sp_name, delete_items="password", with_data=True)
       pass_in = request.data["password"]
       pass_store = ""
       user = UserAuth(id_card="", is_valid=False)
       for items in login.Data:
           print(items)
           for key, value in items.items():
               if "password" in key:
                   pass_store = value
               if "id_card" in key:
                   user.id_card = value
                   user.is_valid = True    

       
       if(login.Status):
            if(Password.validate_password(pass_in, pass_store)):

                return Response(
                    Status= True,
                    Messague= "Sesion iniciada correctamente",
                    Data= []
                )
                
          
            else:
                
                return Response(
                    Status=False,
                    Messague=f"Usuario o contraseña incorrectos",
                    Data= []
                    
                    )

    def create_user(self, request, sp_name, with_data=False):
        
        user_form = {}
        values = []
        for  key, value in request.data.items():
            
            if "password" in key:
                user_form[key] = Password.encrypt(password=value).decode('utf-8')  
            else:
                user_form[key] = value

        for key,value in user_form.items():
            values.append(value)


        return self.call_sp(values, sp_name)

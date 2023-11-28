from ast import List
from numpy import true_divide
from ..ABC.AbsAlterTables import AbsAlterTables
from ..Repository.RepositoryABC import RepositoryABC

from Fruver_api.Response_server.Response import Response
from ..Conexion import conexion

class InventoryRepos(AbsAlterTables, RepositoryABC):
   def __init__(self, conn : conexion) -> None:
      self.conn = conn
      self.res = []
   def create_inventory(self, request, name_sp):
        self.res = []  # Reiniciar la lista antes de cada llamada
        exception_occurred = False
        print(request.data)
        
        for form in request.data:
            try:
                
                values = list(form.values())
                self.res.append(self.conn.execute_cmd(name_sp, values, with_data=True))

            except Exception as e:
                exception_occurred = True
                print(e)
                break  # Salir del bucle al primer error

        if exception_occurred:
            print("Se produjo una excepción. No se completaron todas las iteraciones.")

        return self.res[0]  
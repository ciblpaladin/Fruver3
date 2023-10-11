from ..Conexion import conexion
from ...Services.Map_client_data import Map_data

class RepositoryABC:
    def __init__(self, conn : conexion) -> None:
        self.conn: conexion = conn
        self.model_to_dict = {}


    def get_all(self, sp_reader): 
        
        return self.conn.execute_reader(sp_reader)
    
    def create(self, request, sp_name, with_data = False):

       data_values = Map_data.data_to_sp(request)

       return self.conn.execute_cmd(sp_name, data_values, with_data)
        #return self.conn.execute_cmd(sp_cmd)

    


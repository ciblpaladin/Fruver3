from ..Conexion import conexion
from ...Services.Map_client_data import Map_data

class RepositoryABC:
    def __init__(self, conn : conexion) -> None:
        self.conn: conexion = conn
        self.model_to_dict = {}


    def get_all(self, sp_reader): 
        
        return self.conn.execute_reader(sp_reader)
    
    def create(self, request, sp_name):

       SP_building = Map_data.data_to_sp(request, sp_name)

       return self.conn.execute_cmd(SP_building)
        #return self.conn.execute_cmd(sp_cmd)



from ..Conexion import conexion
from ...Interfaces.Imodel import Imodel

class RepositoryABC:
    def __init__(self, conn : conexion) -> None:
        self.conn: conexion = conn
        self.model_to_dict = {}


    def get_all(self, sp_reader): 
        
        return self.conn.execute_reader(sp_reader)



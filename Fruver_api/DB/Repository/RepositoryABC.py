from ..Conexion import conexion
from ...Interfaces.Imodel import Imodel

class RepositoryABC:
    def __init__(self, conn : conexion) -> None:
        self.conn: conexion = conn



    def get_all(self, sp_reader):
        
       return self.conn.execute_reader(sp_reader)


    def create(self, sp_cmd):

        return self.conn.execute_reader()
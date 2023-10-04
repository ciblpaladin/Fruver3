from ..Conexion import conexion
from ...Services.Map_client_data import Map_data

class AbsAlterTables:

    def __init__(self, conn : conexion) -> None:
        self.conn = conn

    def delete(self, request, sp_name):

        build = Map_data.data_to_sp(request, sp_name)
        
        return self.conn.execute_cmd(build)


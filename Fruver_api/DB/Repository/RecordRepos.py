from ..ABC.AbsAlterTables import AbsAlterTables
from ..Conexion import conexion

class RecordsRepos(AbsAlterTables):

    def __init__(self, conn : conexion) -> None:
        super().__init__(conn=conn)

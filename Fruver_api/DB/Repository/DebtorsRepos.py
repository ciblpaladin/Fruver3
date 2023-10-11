from .RepositoryABC import RepositoryABC
from ..Conexion import conexion
from ...DB.ABC.AbsAlterTables import AbsAlterTables
class DebtorsRepos(RepositoryABC, AbsAlterTables):

    def __init__(self, conn : conexion) -> None:
        super().__init__(conn=conn)

    
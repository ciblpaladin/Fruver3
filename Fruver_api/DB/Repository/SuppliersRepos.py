from .RepositoryABC import RepositoryABC
from ..Conexion import conexion

class SuppliersRepos(RepositoryABC):

    def __init__(self, conn : conexion) -> None:
        super().__init__(conn=conn)

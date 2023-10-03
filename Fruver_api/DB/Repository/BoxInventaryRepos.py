from .RepositoryABC import RepositoryABC
from ..Conexion import conexion
from ...Models.Box_inventary import Box_inventary

class BoxInventaryRepos(RepositoryABC):

    def __init__(self, conn : conexion) -> None:
        super().__init__(conn=conn)


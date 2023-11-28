from .RepositoryABC import RepositoryABC
from ..Conexion import conexion
from ...Models.Box_inventary import Product
from ..ABC.AbsAlterTables import AbsAlterTables

class ProductRepos(RepositoryABC, AbsAlterTables):

    def __init__(self, conn : conexion) -> None:
        super().__init__(conn=conn)


from .RepositoryABC import RepositoryABC
from ..Conexion import conexion
from ...Models.Box_inventary import Product

class ProductRepos(RepositoryABC):

    def __init__(self, conn : conexion) -> None:
        super().__init__(conn=conn)
        self.products : list = []

    def get_products(self):

        data = self.get_all("SP_getProducts()")
            
        for id, product_name, trays_box in data:

            product = Product(
                id=id,
                product_name=product_name, 
                trays_per_box=trays_box)
            
            self.products.append(product.to_dict())

        return self.products
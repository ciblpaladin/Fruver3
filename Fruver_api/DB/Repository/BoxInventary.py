from .RepositoryABC import RepositoryABC
from ..Conexion import conexion
from ...Models.Box_inventary import Box_inventary

class BoxInventaryRepos(RepositoryABC):

    def __init__(self, conn : conexion) -> None:
        super().__init__(conn=conn)
        self.boxs : list = []

    def get_inventary_box(self):

        data = self.get_all("SP_getBoxInventary()")
            
        for id_box, product_name, box_value, date_box_inventary, total_value in data:

            for id_box, product_name, box_value, date_box_inventary, total_value in data:
                box = Box_inventary(
                    id_box=id_box,
                    product_name=product_name,
                    amount=box_value,
                    box_value=date_box_inventary,  # Asigna box_value a sí mismo
                    total_value=total_value,  # Asigna total_value a sí mismo
                    user_fk=None,  # Asegúrate de proporcionar un valor válido para user_fk
                )
            
            self.products.append(product.to_dict())

        return self.products
from ..Interfaces.Imodel import Imodel
from dataclasses import dataclass

@dataclass
class Box_inventary(Imodel):

    id_box: int  
    product_name: str  
    amount : int  
    box_value  : float
    total_value   : float
    user_fk : int
    def to_dict(self):
        return {

            "id_box" : self.id_box,
            "product_name" : self.product_name,
            "amount" : self.amount,
            "box_value" : self.box_value,
            "total_value" : self.total_value,
            "user_fk" : self.user_fk,
        } 

@dataclass
class Product(Imodel):
    
    id : int
    product_name : str
    trays_per_box : int

    def to_dict(self):
        return {

            "id" : self.id,
            "product_name" : self.product_name,
            "trays_per_box" : self.trays_per_box
        }     
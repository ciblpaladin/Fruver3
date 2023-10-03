from ..Interfaces.Imodel import Imodel
from dataclasses import dataclass

@dataclass
class Box_inventary(Imodel):
    id_box: int  
    product_name: str  
    amount : int  
    box_value  : float
    date_box_inventary : str
    total_value  : float
    id_user : int
    names_ : str
    lastnames : str


@dataclass
class Product(Imodel):
    
    id : int
    product_name : str
    trays_per_box : int

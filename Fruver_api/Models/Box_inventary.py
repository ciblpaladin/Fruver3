from ..Interfaces.Imodel import Imodel
from dataclasses import dataclass
from rest_framework_simplejwt.models import TokenUser
from ..DB.Repository.RepositoryABC import RepositoryABC
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


class UserAuth():
    
    id_card : int
    #password : str
    is_valid : bool
    
    def get_token_user(self,cls, user):
        
        print("ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        return cls(id_card=user.id_card, is_valid=user.is_valid)
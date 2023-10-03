from abc import ABC, abstractmethod

class Imodel(ABC):
    
    @abstractmethod
    def to_dict(self):
        pass
from dataclasses import dataclass
@dataclass
class Response:

    Status : bool
    Messague : str
    Data : list

    def to_dict(self):
        return {

            "Status" : self.Status,
            "Messague" : self.Messague,
            "Data" : self.Data
        }
from pydantic import BaseModel
from datetime import date
from typing import Optional, List


class MedicamentBaseSchema(BaseModel) :
    nom: str
    date_expiration: date
    prix_unitaire: str
    

class MedicamentSchema(MedicamentBaseSchema) :
    id: int


class MedicamentCreateSchema(MedicamentBaseSchema) :
    date_expiration: date = date.today()


class MedicamentUpdateSchema(MedicamentBaseSchema) :
    nom: Optional[str] = None
    date_expiration: Optional[date] = None
    prix_unitaire: Optional[str] = None


class StockBaseSchema(BaseModel) :
    quantite_disponible: int
    quantite_entree: int
    quantite_sortie: int
    date_mouvement: date
    prix_unitaire: str
    medicament_id: int    


class StockSchema(StockBaseSchema):
    id: int


class StockCreateSchema(StockBaseSchema):
    date_mouvement: date = date.today()


class StockUpdateSchema(BaseModel) :
    quantite_disponible: Optional[int] = None
    quantite_entree: Optional[int] = None
    quantite_sortie: Optional[int] = None
    date_mouvement: Optional[date] = None
    prix_unitaire: Optional[str] = None
    medicament_id: Optional[int] = None        


#---------------------------
#     Detailed Schema
#---------------------------

class MedicamentDetailedSchema(MedicamentBaseSchema) :
    from schemas.medical import PrescriptionSchema as _PrescriptionSchema
    id: int
    stocks: List[StockSchema]
    prescriptions: List[_PrescriptionSchema]


class StockDetailedSchema(StockBaseSchema):
    id: int
    medicament: MedicamentSchema


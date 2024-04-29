from pydantic import BaseModel
from datetime import date
from typing import Optional, List


class FactureSchema(BaseModel) :
    id: int
    date_emission: date
    montant_total: str
    type_service: str
    patient_id: int


class FactureCreateSchema(BaseModel) :
    date_emission: date = date.today()
    montant_total: str
    type_service: str
    patient_id: int


class FactureUpdateSchema(BaseModel) :
    date_emission: Optional[date] = None
    montant_total: Optional[str] = None
    type_service: Optional[str] = None
    patient_id: Optional[int] = None


class DetailsFactureSchema(BaseModel) :
    id: int
    description: str
    quantite: int
    prix_unitaire: str
    facture_id: int


class DetailsFactureCreateSchema(BaseModel) :
    description: str
    quantite: int
    prix_unitaire: str
    facture_id: int


class DetailsFactureUpdateSchema(BaseModel) :
    description: Optional[str] = None
    quantite: Optional[int] = None
    prix_unitaire: Optional[str] = None
    facture_id: Optional[int] = None


#------------------------------
#      Detailed schema
#------------------------------

class FactureDetailedSchema(BaseModel) :
    from schemas.patient import PatientSchema as _PatientSchema
    id: int
    date_emission: date
    montant_total: str
    type_service: str
    patient_id: int
    details_facture: List[DetailsFactureSchema]
    patient: _PatientSchema


class DetailsFactureDetailedSchema(BaseModel) :
    id: int
    description: str
    quantite: int
    prix_unitaire: str
    facture_id: int
    facture: FactureSchema

from pydantic import BaseModel
from typing import Optional
from schemas.patient import ChambreSchema
from schemas.utilisateur import InfirmierSchema
from schemas.operation import ActeChirurgicalSchema
from schemas.utilisateur import EmployeSchema
from schemas.pharmacie import MedicamentSchema
from schemas.medical import PrescriptionSchema


# First
class AssociationChambreInfirmierSchema(BaseModel) :
    chambre_id: int
    infirmier_id: int


class AssociationChambreInfirmierDetailedSchema(BaseModel) :
    chambre_id: int
    infirmier_id: int
    chambre: ChambreSchema
    infirmier: InfirmierSchema


class AssociationChambreInfirmierCreateSchema(BaseModel) :
    chambre_id: int
    infirmier_id: int



class AssociationChambreInfirmierUpdateSchema(BaseModel) :
    chambre_id: Optional[int]
    infirmier_id: Optional[int]


# Second
class AssociationActeChirurgicalEmployeSchema(BaseModel) :
    acte_chirurgical_id: int
    employe_id: int


class AssociationActeChirurgicalEmployeDetailedSchema(BaseModel) :
    acte_chirurgical_id: int
    employe_id: int
    acte_chirurgical: ActeChirurgicalSchema
    employe: EmployeSchema


class AssociationActeChirurgicalEmployeCreateSchema(BaseModel) :
    acte_chirurgical_id: int
    employe_id: int


class AssociationActeChirurgicalEmployeUpdateSchema(BaseModel) :
    acte_chirurgical_id: Optional[int]
    employe_id: Optional[int]


# Third
class AssociationMedicamentPrescriptionSchema(BaseModel) :
    medicament_id: int
    prescription_id: int


class AssociationMedicamentPrescriptionDetailedSchema(BaseModel) :
    medicament_id: int
    prescription_id: int
    medicament: MedicamentSchema
    prescription: PrescriptionSchema


class AssociationMedicamentPrescriptionCreateSchema(BaseModel) :
    medicament_id: int
    prescription_id: int


class AssociationMedicamentPrescriptionUpdateSchema(BaseModel) :
    medicament_id: Optional[int]
    prescription_id: Optional[int]


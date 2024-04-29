from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class EmployeSchema(BaseModel) :
    id: int
    nom: str
    postnom: str
    prenom: str
    adresse_physique: str
    horaire_travail: str   # Avant midi, après-midi, matin; nuit...


class EmployeCreateSchema(BaseModel) :
    nom: str
    postnom: str
    prenom: str
    adresse_physique: str
    horaire_travail: str = ''


class EmployeUpdateSchema(BaseModel) :
    nom: Optional[str] = None
    postnom: Optional[str] = None
    prenom: Optional[str] = None
    adresse_physique: Optional[str] = None
    horaire_travail: Optional[str] = None


class MedecinSchema(BaseModel) :
    id: int
    specialisation: str
    employe_id: int


class MedecinCreateSchema(BaseModel) :
    specialisation: str
    employe_id: int


class MedecinUpdateSchema(BaseModel) :
    specialisation: Optional[str] = None
    employe_id: Optional[int] = None


class ReceptionnisteSchema(BaseModel) :
    id: int
    employe_id: int


class ReceptionnisteCreateSchema(BaseModel) :
    employe_id: int


class ReceptionnisteUpdateSchema(BaseModel) :
    employe_id: Optional[int] = None


class PharmacienSchema(BaseModel) :
    id: int
    employe_id: int


class PharmacienCreateSchema(BaseModel) :
    employe_id: int


class PharmacienUpdateSchema(BaseModel) :
    employe_id: Optional[int] = None


class InfirmierSchema(BaseModel) :
    id: int
    employe_id: int


class InfirmierCreateSchema(BaseModel) :
    employe_id: int


class InfirmierUpdateSchema(BaseModel) :
    employe_id: Optional[int] = None


class CaissierSchema(BaseModel):
    id: int
    employe_id: int
    numero_caisse: int


class CaissierCreateSchema(BaseModel) :
    employe_id: int
    numero_caisse: int = 0


class CaissierUpdateSchema(BaseModel) :
    employe_id: Optional[int] = None
    numero_caisse: Optional[int] = None


class CompteSchema(BaseModel):
    id: int
    username: str
    passeword: str
    date_derniere_connexion: datetime
    email: str
    role: str
    status: str                # actif, inactif, bloqué
    employe_id: int


class CompteCreateSchema(BaseModel) :
    username: str
    passeword: str
    date_derniere_connexion: datetime = datetime.now()
    email: str
    role: str
    status: str           
    employe_id: int


class CompteUpdateSchema(BaseModel) :
    username: Optional[str] = None
    passeword: Optional[str] = None
    date_derniere_connexion: Optional[datetime] = None
    email: Optional[str] = None
    role: Optional[str] = None
    status: Optional[str] = None         
    employe_id: Optional[int] = None



#---------------------------
#     Detailed schema
#---------------------------
    
class EmployeDetailedSchema(BaseModel) :
    from schemas.operation import ActeChirurgicalSchema as _ActeChirurgicalSchema
    from schemas.association import AssociationActeChirurgicalEmployeSchema as _AssociationActeChirurgicalEmployeSchema
    id: int
    nom: str
    postnom: str
    prenom: str
    adresse_physique: str
    horaire_travail: str

    receptionniste: Optional[ReceptionnisteSchema]
    pharmacien: Optional[PharmacienSchema]
    medecin: Optional[MedecinSchema]
    caissier: Optional[CaissierSchema]
    infirmier: Optional[InfirmierSchema]
    compte: Optional[CompteSchema]

    actes_chirurgicals: List[_AssociationActeChirurgicalEmployeSchema]


class MedecinDetailedSchema(BaseModel) :
    from schemas.medical import FicheConsultationSchema as _FicheConsultationSchema
    from schemas.operation import (ReceptionSchema as _ReceptionSchema, 
                                   ActeChirurgicalSchema as _ActeChirurgicalSchema)
    id: int
    specialisation: str
    employe_id: int
    employe: EmployeSchema
    fiches_consultations: List[_FicheConsultationSchema]
    receptions: List[_ReceptionSchema]
    actes_chirurgicals: List[_ActeChirurgicalSchema]


class InfirmierDetailedSchema(BaseModel) :
    from schemas.patient import ChambreSchema as _ChambreSchema
    id: int
    employe_id: int
    employe: EmployeSchema
    chambres: List[_ChambreSchema]


class ReceptionnisteDetailedSchema(BaseModel) :
    id: int
    employe_id: int
    employe: EmployeSchema


class PharmacienDetailedSchema(BaseModel) :
    id: int
    employe_id: int
    employe: EmployeSchema


class CaissierDetailedSchema(BaseModel):
    id: int
    employe_id: int
    numero_caisse: int
    employe: EmployeSchema


class CompteDetailedSchema(BaseModel):
    id: int
    username: str
    passeword: str
    date_derniere_connexion: datetime
    email: str
    role: str
    status: str
    employe_id: int
    employe: EmployeSchema

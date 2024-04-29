from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ReceptionSchema(BaseModel) :
    id: int 
    nom: str
    postnom: str
    prenom: str
    heure_arrive: datetime
    recu: bool                  # Yes or No
    medecin_id: Optional[int]


class ReceptionCreateSchema(BaseModel) :
    nom: str
    postnom: str
    prenom: str
    heure_arrive: datetime = datetime.now()
    recu: bool                  # Yes or No
    medecin_id: Optional[int] = None    


class ReceptionUpdateSchema(BaseModel) :
    nom: Optional[str] = None
    postnom: Optional[str] = None
    prenom: Optional[str] = None
    heure_arrive: Optional[datetime] = None
    recu: Optional[bool] = None
    medecin_id: Optional[int] = None    


class ActeChirurgicalSchema(BaseModel) :
    id: int
    type_chirurgie: str
    debut: datetime
    duree_operation: int
    complications_eventuelles: str
    anesthesie_utilise: str
    patient_id: int
    chirurgien_principal_id: int   


class ActeChirurgicalCreateSchema(BaseModel):
    type_chirurgie: str
    debut: datetime = datetime.now()
    duree_operation: int
    complications_eventuelles: str = ''
    anesthesie_utilise: str = ''
    patient_id: int
    chirurgien_principal_id: int


class ActeChirurgicalUpdateSchema(BaseModel):
    type_chirurgie: Optional[str] = None
    debut: Optional[datetime] = None
    duree_operation: Optional[int] = None
    complications_eventuelles: Optional[str] = None
    anesthesie_utilise: Optional[str] = None
    patient_id: Optional[int] = None
    chirurgien_principal_id: Optional[int] = None


#---------------------------
#     Detailed Schema
#---------------------------

class ReceptionDetailedSchema(BaseModel) :
    from schemas.utilisateur import MedecinSchema as _MedecinSchema
    id: int 
    nom: str
    postnom: str
    prenom: str
    heure_arrive: datetime
    recu: bool                  # Yes or No
    medecin_id: Optional[int]    
    medecin: Optional[_MedecinSchema]


class ActeChirurgicalDetailedSchema(BaseModel):
    from schemas.utilisateur import (MedecinSchema as _EmployeSchema, 
                                     EmployeSchema as _EmployeSchema)
    id: int
    type_chirurgie: str
    debut: datetime
    duree_operation: int
    complications_eventuelles: str
    anesthesie_utilise: str
    patient_id: int
    chirurgien_principal_id: int 
    chirurgien_principal: _EmployeSchema
    assistants: _EmployeSchema

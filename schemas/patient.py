from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List
from fastapi import UploadFile


class PatientBaseSchema(BaseModel) :
    nom: str
    postnom: str
    prenom: str
    adresse: str
    numero_telephone: str
    age: int
    poids: int
    sexe: str
    date_naissance: date
    lieu_naissance: str
    profession: str
    etat_civil: str


class PatientCreateSchema(PatientBaseSchema) :
    fichier: UploadFile


class PatientSchema(PatientBaseSchema) :
    id: int
    chemin_fichier: str


class PatientUpdateSchema(BaseModel) :
    nom: Optional[str] = None
    postnom: Optional[str] = None
    prenom: Optional[str] = None
    adresse: Optional[str] = None
    numero_telephone: Optional[str] = None
    age: Optional[int] = None
    poids: Optional[int] = None
    sexe: Optional[str] = None
    date_naissance: Optional[date] = None
    lieu_naissance: Optional[str] = None
    profession: Optional[str] = None
    etat_civil: Optional[str] = None
    fichier: Optional[UploadFile] = None


class HospitalisationBaseSChema(BaseModel) :
    date_entree: datetime
    date_sortie: datetime
    motif: str
    patient_id: int
    chambre_id: int
    service_medical_id: int   


class HospitalisationSchema(HospitalisationBaseSChema) :
    id: int 


class HospitalisationCreateSchema(HospitalisationBaseSChema) :
    date_entree: datetime = datetime.now()
    date_sortie: datetime = datetime.now()


class HospitalisationUpdateSchema(BaseModel) :
    date_entree: Optional[datetime] = None
    date_sortie: Optional[datetime] = None
    motif: Optional[str] = None
    patient_id: Optional[int] = None
    chambre_id: Optional[int] = None
    service_medical_id: Optional[int] = None


class ChambreBaseSchema(BaseModel) :
    numero_chambre: int
    status: bool            # Occupé ou libre



class ChambreSchema(ChambreBaseSchema) :
    id: int


class ChambreCreateSchema(ChambreBaseSchema) :
    pass


class ChambreUpdateSchema(BaseModel) :
    numero_chambre: Optional[int] = None
    status: Optional[bool] = None


#---------------------------
#     Detailed Schema
#---------------------------

class PatientDetailedSchema(PatientBaseSchema) :
    from schemas.medical import (ImageMedicalSchema as _ImageMedicalSchema, 
                                 ExamenPhysiqueSchema as _ExamenPhysiqueSchema,
                                 FicheConsultationSchema as _FicheConsultationSchema, 
                                 OrdonnanceSchema as _OrdonnanceSchema)
    from schemas.finance import FactureSchema as _FactureSchema
    from schemas.operation import ActeChirurgicalSchema as _ActeChirurgicalSchema
    id: int
    chemin_fichier: str
    actes_chirurgicales: List[_ActeChirurgicalSchema]
    factures: List[_FactureSchema]
    hospitalisations: List[HospitalisationSchema]
    images_medicales: List[_ImageMedicalSchema]
    examens_physiques: List[_ExamenPhysiqueSchema]
    fiches_consultations: List[_FicheConsultationSchema]
    ordonnances: List[_OrdonnanceSchema]


class HospitalisationDetailedSchema(HospitalisationBaseSChema) :
    from schemas.medical import ServiceMedicalSchema as _ServiceMedicalSchema
    id: int 
    patient: PatientSchema
    chambre: ChambreSchema
    service_medical: _ServiceMedicalSchema


class ChambreDetailedSchema(ChambreBaseSchema) :
    from schemas.utilisateur import InfirmierSchema as _InfirmierSchema
    id: int
    hospitalisation: HospitalisationSchema
    infirmiers: List[_InfirmierSchema]

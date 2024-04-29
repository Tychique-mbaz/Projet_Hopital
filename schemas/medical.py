from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List
from fastapi import UploadFile


class OrdonnanceSchema(BaseModel) :
    id: int
    date_emission: datetime 
    designation: str
    indications: str
    patient_id: int
                        

class OrdonnanceCreateSchema(BaseModel) :
    date_emission: datetime = datetime.now()
    designation: str
    indications: str
    patient_id: int


class OrdonnanceUpdateSchema(BaseModel) :
    date_emission: Optional[datetime] = None
    designation: Optional[str] = None
    indications: Optional[str] = None
    patient_id: Optional[int] = None


class FicheConsultationSchema(BaseModel) :
    id: int
    motif_consultation: str
    etat_vaccinal: str                    # Rhume, toux
    prise_charge_medical_et_psychosociale: str
    date_emission: datetime
    patient_id: int
    medecin_id: int    


class FicheConsultationCreateSchema(BaseModel) :
    motif_consultation: str
    etat_vaccinal: str                         # Rhume, toux
    prise_charge_medical_et_psychosociale: str
    date_emission: datetime = datetime.now()
    patient_id: int
    medecin_id: int


class FicheConsultationUpdateSchema(BaseModel) :
    motif_consultation: Optional[str] = None
    etat_vaccinal: Optional[str] = None                        # Rhume, toux
    prise_charge_medical_et_psychosociale: Optional[str] = None
    date_emission: Optional[datetime] = None
    patient_id: Optional[int] = None
    medecin_id: Optional[int] = None


class PrescriptionSchema(BaseModel) :
    id: int
    posologie: str
    date_prescription: date
    quantite: int
    fiche_consultation_id: int


class PrescriptionCreateSchema(BaseModel) :
    posologie: str
    date_prescription: date = date.today()
    quantite: int
    fiche_consultation_id: int


class PrescriptionUpdateSchema(BaseModel) : 
    posologie: Optional[str] = None
    date_prescription: Optional[date] = None
    quantite: Optional[int] = None
    fiche_consultation_id: Optional[int] = None


class AntecedentSchema(BaseModel) :
    id: int
    question: str
    reponse: str
    fiche_consultation_id: int


class AntecedentCreateSchema(BaseModel) :
    question: str
    reponse: str
    fiche_consultation_id: int


class AntecedentUpdateSchema(BaseModel) :
    question: Optional[str] = None
    reponse: Optional[str] = None
    fiche_consultation_id: Optional[int] = None


class SigneVitalSchema(BaseModel) :
    id: int
    nom_signe: str        # Pouls, Fr, glycémie
    valeur: str
    date_heure_mesure: datetime
    fiche_consultation_id: int
    

class SigneVitalCreateSchema(BaseModel) :
    nom_signe: str        # Pouls, Fr, glycémie
    valeur: str
    date_heure_mesure: datetime = datetime.now()
    fiche_consultation_id: int


class SigneVitalUpdateSchema(BaseModel) :
    nom_signe: Optional[str] = None        # Pouls, Fr, glycémie
    valeur: Optional[str] = None
    date_heure_mesure: Optional[datetime] = None
    fiche_consultation_id: Optional[int] = None


class ExamenPhysiqueSchema(BaseModel) :
    id: int
    type_examen: str
    resultat: str
    date_realisation: datetime
    fiche_consultation_id: Optional[int] = None
    patient_id: Optional[int] = None


class ExamenPhysiqueCreateSchema(BaseModel) :
    type_examen: str
    resultat: str
    date_realisation: datetime = datetime.now()
    fiche_consultation_id: Optional[int] = None
    patient_id: Optional[int] = None


class ExamenPhysiqueUpdateSchema(BaseModel) :
    type_examen: Optional[str] = None
    resultat: Optional[str] = None
    date_realisation: Optional[datetime] = None
    fiche_consultation_id: Optional[int] = None
    patient_id: Optional[int] = None


class ServiceMedicalSchema(BaseModel) :
    id: int
    nom_service: str     # Néonatologie, Medecine interne (Homme & Femme)...


class ServiceMedicalCreateSchema(BaseModel) :
    nom_service: str    


class ServiceMedicalUpdateSchema(BaseModel) :
    nom_service: Optional[str] = None


class ImageMedicalSchema(BaseModel) :
    id: int
    type_image: str     # IRM, radiographie, échographie
    date_prise: datetime 
    chemin_fichier: str
    patient_id: int


class ImageMedicalCreateSchema(BaseModel) :
    type_image: str     # IRM, radiographie, échographie
    date_prise: datetime = datetime.now() 
    patient_id: int
    fichier: UploadFile


class ImageMedicalUpdateSchema(BaseModel) :
    type_image: Optional[str] = None     # IRM, radiographie, échographie
    date_prise: Optional[datetime] = None 
    fichier: Optional[UploadFile] = None
    patient_id: Optional[int] = None


class ParacliniqueEssentielleSchema(BaseModel) :
    id: int
    intitule: str
    reponse: str
    fiche_consultation_id: Optional[int] = None 
    image_medical_id: Optional[int] = None
    

class ParacliniqueEssentielleCreateSchema(BaseModel) :
    intitule: str
    reponse: str
    fiche_consultation_id: Optional[int] = None 
    image_medical_id: Optional[int] = None


class ParacliniqueEssentielleUpdateSchema(BaseModel) :
    intitule: Optional[str] = None
    reponse: Optional[str] = None
    fiche_consultation_id: Optional[int] = None 
    image_medical_id: Optional[int] = None


#---------------------------
#     Detailed Schema
#---------------------------

class FicheConsultationDetailedSchema(BaseModel) :
    from schemas.utilisateur import MedecinSchema as _MedecinSchema
    from schemas.patient import PatientSchema as _PatientSchema
    id: int
    motif_consultation: str
    etat_vaccinal: str                    # Rhume, toux
    prise_charge_medical_et_psychosociale: str
    date_emission: datetime
    patient_id: int
    medecin_id: int    
    patient: _PatientSchema
    medecin: _MedecinSchema
    
    prescriptions: List[PrescriptionSchema]
    antecedents: List[AntecedentSchema]
    signes_vitaux: List[SigneVitalSchema]
    examens_physiques: List[ExamenPhysiqueSchema]
    paracliniques_essentielles: List[ParacliniqueEssentielleSchema]


class OrdonnanceDetailedSchema(BaseModel) :
    from schemas.patient import PatientSchema as _PatientSchema
    id: int
    date_emission: datetime 
    designation: str
    indications: str
    patient_id: int
    patient: _PatientSchema


class ParacliniqueEssentielleDetailedSchema(BaseModel) :
    id: int
    intitule: str
    reponse: str
    fiche_consultation_id: Optional[int] = None 
    fiche_consultation: Optional[FicheConsultationSchema] = None
    image_medical_id: Optional[int] = None
    image_medical: Optional[ImageMedicalSchema] = None


class ImageMedicalDetailedSchema(BaseModel) :
    from schemas.patient import PatientSchema as _PatientSchema
    id: int
    type_image: str     # IRM, radiographie, échographie
    date_prise: datetime 
    chemin_fichier: str
    patient_id: int
    patient: _PatientSchema
    paraclinique_essentielle: ParacliniqueEssentielleSchema


class ServiceMedicalDetailedSchema(BaseModel) :
    from schemas.patient import HospitalisationSchema as _HospitalisationSchema
    id: int
    nom_service: str     # Néonatologie, Medecine interne (Homme & Femme)...
    hospitalisations: List[_HospitalisationSchema]


class ExamenPhysiqueDetailedSchema(BaseModel) :
    from schemas.patient import PatientSchema as _PatientSchema
    id: int
    type_examen: str
    resultat: str
    date_realisation: datetime
    fiche_consultation_id: Optional[int] = None
    fiche_consultation: Optional[FicheConsultationSchema] = None
    patient_id: Optional[int] = None
    patient: Optional[_PatientSchema] = None


class PrescriptionDetailedSchema(BaseModel) :
    from schemas.pharmacie import MedicamentSchema as _MedicamentSchema
    id: int
    posologie: str
    date_prescription: date
    quantite: int
    fiche_consultation_id: int
    fiche_consultation: FicheConsultationSchema
    medicaments: List[_MedicamentSchema]

    
class AntecedentDetailedSchema(BaseModel) :
    id: int
    question: str
    reponse: str
    fiche_consultation_id: int
    fiche_consultation: FicheConsultationSchema


class SigneVitalDetailedSchema(BaseModel) :
    id: int
    nom_signe: str        # Pouls, Fr, glycémie
    valeur: str
    date_heure_mesure: datetime
    fiche_consultation_id: int
    fiche_consultation: FicheConsultationSchema


from routes.crud_router import CRUDRouter
from database.tables.medical import (
    Ordonnance,
    FicheConsultation,
    Prescription,
    Antecedent,
    SigneVital,
    ExamenPhysique,
    ServiceMedical,
    ImageMedical,
    ParacliniqueEssentielle,
)
from database.base import get_db
from schemas.medical import (
    OrdonnanceSchema,
    OrdonnanceDetailedSchema,
    OrdonnanceCreateSchema,
    OrdonnanceUpdateSchema,
    FicheConsultationSchema,
    FicheConsultationDetailedSchema,
    FicheConsultationCreateSchema,
    FicheConsultationUpdateSchema,
    PrescriptionSchema,
    PrescriptionDetailedSchema,
    PrescriptionCreateSchema,
    PrescriptionUpdateSchema,
    AntecedentSchema,
    AntecedentDetailedSchema,
    AntecedentCreateSchema,
    AntecedentUpdateSchema,
    SigneVitalSchema,
    SigneVitalDetailedSchema,
    SigneVitalCreateSchema,
    SigneVitalUpdateSchema,
    ExamenPhysiqueSchema,
    ExamenPhysiqueDetailedSchema,
    ExamenPhysiqueCreateSchema,
    ExamenPhysiqueUpdateSchema,
    ServiceMedicalSchema,
    ServiceMedicalDetailedSchema,
    ServiceMedicalCreateSchema,
    ServiceMedicalUpdateSchema,
    ImageMedicalSchema,
    ImageMedicalDetailedSchema,
    ImageMedicalCreateSchema,
    ImageMedicalUpdateSchema,
    ParacliniqueEssentielleSchema,
    ParacliniqueEssentielleDetailedSchema,
    ParacliniqueEssentielleCreateSchema,
    ParacliniqueEssentielleUpdateSchema,
)


ordonnance_router = CRUDRouter(
    schema=OrdonnanceSchema,
    schema_detailed=OrdonnanceDetailedSchema,
    create_schema=OrdonnanceCreateSchema,
    update_schema=OrdonnanceUpdateSchema,
    db_session=get_db,
    db_model=Ordonnance,
    prefix='ordonnance',
    page_size=10,
)


fiche_consultation_router = CRUDRouter(
    schema=FicheConsultationSchema,
    schema_detailed=FicheConsultationDetailedSchema,
    create_schema=FicheConsultationCreateSchema,
    update_schema=FicheConsultationUpdateSchema,
    db_session=get_db,
    db_model=FicheConsultation,
    prefix='fiche_consultation',
    page_size=10,
)


prescription_router = CRUDRouter(
    schema=PrescriptionSchema,
    schema_detailed=PrescriptionDetailedSchema,
    create_schema=PrescriptionCreateSchema,
    update_schema=PrescriptionUpdateSchema,
    db_session=get_db,
    db_model=Prescription,
    prefix='prescription',
    page_size=10,
)


antecedent_router = CRUDRouter(
    schema=AntecedentSchema,
    schema_detailed=AntecedentDetailedSchema,
    create_schema=AntecedentCreateSchema,
    update_schema=AntecedentUpdateSchema,
    db_session=get_db,
    db_model=Antecedent,
    prefix='antecedent',
    page_size=10,
)


signe_vital_router = CRUDRouter(
    schema=SigneVitalSchema,
    schema_detailed=SigneVitalDetailedSchema,
    create_schema=SigneVitalCreateSchema,
    update_schema=SigneVitalUpdateSchema,
    db_session=get_db,
    db_model=SigneVital,
    prefix='signe_vital',
    page_size=10,
)


examen_physique_router = CRUDRouter(
    schema=ExamenPhysiqueSchema,
    schema_detailed=ExamenPhysiqueDetailedSchema,
    create_schema=ExamenPhysiqueCreateSchema,
    update_schema=ExamenPhysiqueUpdateSchema,
    db_session=get_db,
    db_model=ExamenPhysique,
    prefix='examen_physique',
    page_size=10,
)


service_medical_router = CRUDRouter(
    schema=ServiceMedicalSchema,
    schema_detailed=ServiceMedicalDetailedSchema,
    create_schema=ServiceMedicalCreateSchema,
    update_schema=ServiceMedicalUpdateSchema,
    db_session=get_db,
    db_model=ServiceMedical,
    prefix='service_medical',
    page_size=10,
)


image_medical_router = CRUDRouter(
    schema=ImageMedicalSchema,
    schema_detailed=ImageMedicalDetailedSchema,
    create_schema=ImageMedicalCreateSchema,
    update_schema=ImageMedicalUpdateSchema,
    db_session=get_db,
    db_model=ImageMedical,
    prefix='image_medical',
    page_size=10,
    file_path='media/images_medicales'
)


paraclinique_essentielle_router = CRUDRouter(
    schema=ParacliniqueEssentielleSchema,
    schema_detailed=ParacliniqueEssentielleDetailedSchema,
    create_schema=ParacliniqueEssentielleCreateSchema,
    update_schema=ParacliniqueEssentielleUpdateSchema,
    db_session=get_db,
    db_model=ParacliniqueEssentielle,
    prefix='paraclinique_essentielle',
    page_size=10,
)

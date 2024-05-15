from database.tables.patient import Patient, Hospitalisation, Chambre
from database.base import get_db
from schemas.patient import (
    PatientSchema,
    PatientDetailedSchema,
    PatientCreateSchema,
    PatientUpdateSchema,
    HospitalisationSchema,
    HospitalisationDetailedSchema,
    HospitalisationCreateSchema,
    HospitalisationUpdateSchema,
    ChambreSchema,
    ChambreDetailedSchema,
    ChambreCreateSchema,
    ChambreUpdateSchema,
)
from routes.crud_router import CRUDRouter


patient_router = CRUDRouter(
    schema=PatientSchema,
    schema_detailed=PatientDetailedSchema,
    create_schema=PatientCreateSchema,
    update_schema=PatientUpdateSchema,
    db_session=get_db,
    db_model=Patient,
    prefix='patient',
    page_size=10,
    file_path='media/patients/profiles'
)


hospitalisation_router = CRUDRouter(
    schema=HospitalisationSchema,
    schema_detailed=HospitalisationDetailedSchema,
    create_schema=HospitalisationCreateSchema,
    update_schema=HospitalisationUpdateSchema,
    db_session=get_db,
    db_model=Hospitalisation,
    prefix='hospitalisation',
    page_size=10,
)


chambre_router = CRUDRouter(
    schema=ChambreSchema,
    schema_detailed=ChambreDetailedSchema,
    create_schema=ChambreCreateSchema,
    update_schema=ChambreUpdateSchema,
    db_session=get_db,
    db_model=Chambre,
    prefix='chambre',
    page_size=10,
)

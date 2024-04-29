from schemas.association import (
    AssociationChambreInfirmierSchema,
    AssociationChambreInfirmierDetailedSchema,
    AssociationChambreInfirmierCreateSchema,
    AssociationChambreInfirmierUpdateSchema,
    AssociationActeChirurgicalEmployeSchema,
    AssociationActeChirurgicalEmployeDetailedSchema,
    AssociationActeChirurgicalEmployeCreateSchema,
    AssociationActeChirurgicalEmployeUpdateSchema,
    AssociationMedicamentPrescriptionSchema,
    AssociationMedicamentPrescriptionDetailedSchema,
    AssociationMedicamentPrescriptionCreateSchema,
    AssociationMedicamentPrescriptionUpdateSchema
)
from routes.crud_router import CRUDRouter
from database.tables.association import (
    AssociationChambreInfirmier, 
    AssociationMedicamentPrescription, 
    AssociationActeChirurgicalEmploye
)
from database.base import get_db


a_chambre_infirmier_router = CRUDRouter(
    schema=AssociationChambreInfirmierSchema,
    schema_detailed=AssociationChambreInfirmierDetailedSchema,
    create_schema=AssociationChambreInfirmierCreateSchema,
    update_schema=AssociationChambreInfirmierUpdateSchema,
    db_session=get_db,
    db_model=AssociationChambreInfirmier,
    prefix='a_chambre_infirmier',
    page_size=10,
)


a_acte_chirurgical_employe_router = CRUDRouter(
    schema=AssociationActeChirurgicalEmployeSchema,
    schema_detailed=AssociationActeChirurgicalEmployeDetailedSchema,
    create_schema=AssociationActeChirurgicalEmployeCreateSchema,
    update_schema=AssociationActeChirurgicalEmployeUpdateSchema,
    db_session=get_db,
    db_model=AssociationActeChirurgicalEmploye,
    prefix='a_acte_chirurgical_employe',
    page_size=10,
)


a_medicament_prescription_router = CRUDRouter(
    schema=AssociationMedicamentPrescriptionSchema,
    schema_detailed=AssociationMedicamentPrescriptionDetailedSchema,
    create_schema=AssociationMedicamentPrescriptionCreateSchema,
    update_schema=AssociationMedicamentPrescriptionUpdateSchema,
    db_session=get_db,
    db_model=AssociationMedicamentPrescription,
    prefix='a_medicament_prescription',
    page_size=10,
)
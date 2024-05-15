from routes.crud_router import CRUDRouter
from database.tables.utilisateur import (
    Employe,
    Medecin,
    Receptionniste,
    Pharmacien,
    Infirmier,
    Caissier,
    Compte,
)
from database.base import get_db
from schemas.utilisateur import (
    EmployeSchema,
    EmployeDetailedSchema,
    EmployeCreateSchema,
    EmployeUpdateSchema,
    MedecinSchema,
    MedecinDetailedSchema,
    MedecinCreateSchema,
    MedecinUpdateSchema,
    ReceptionnisteSchema,
    ReceptionnisteDetailedSchema,
    ReceptionnisteCreateSchema,
    ReceptionnisteUpdateSchema,
    PharmacienSchema,
    PharmacienDetailedSchema,
    PharmacienCreateSchema,
    PharmacienUpdateSchema,
    InfirmierSchema,
    InfirmierDetailedSchema,
    InfirmierCreateSchema,
    InfirmierUpdateSchema,
    CaissierSchema,
    CaissierDetailedSchema,
    CaissierCreateSchema,
    CaissierUpdateSchema,
    CompteSchema,
    CompteDetailedSchema,
    CompteCreateSchema,
    CompteUpdateSchema,
)

from routes.crud_router import CRUDRouter

employe_router = CRUDRouter(
    schema=EmployeSchema,
    schema_detailed=EmployeDetailedSchema,
    create_schema=EmployeCreateSchema,
    update_schema=EmployeUpdateSchema,
    db_session=get_db,
    db_model=Employe,
    prefix='employe',
    page_size=10,
)

medecin_router = CRUDRouter(
    schema=MedecinSchema,
    schema_detailed=MedecinDetailedSchema,
    create_schema=MedecinCreateSchema,
    update_schema=MedecinUpdateSchema,
    db_session=get_db,
    db_model=Medecin,
    prefix='medecin',
    page_size=10,
)

receptionniste_router = CRUDRouter(
    schema=ReceptionnisteSchema,
    schema_detailed=ReceptionnisteDetailedSchema,
    create_schema=ReceptionnisteCreateSchema,
    update_schema=ReceptionnisteUpdateSchema,
    db_session=get_db,
    db_model=Receptionniste,
    prefix='receptionniste',
    page_size=10,
)

pharmacien_router = CRUDRouter(
    schema=PharmacienSchema,
    schema_detailed=PharmacienDetailedSchema,
    create_schema=PharmacienCreateSchema,
    update_schema=PharmacienUpdateSchema,
    db_session=get_db,
    db_model=Pharmacien,
    prefix='pharmacien',
    page_size=10,
)

infirmier_router = CRUDRouter(
    schema=InfirmierSchema,
    schema_detailed=InfirmierDetailedSchema,
    create_schema=InfirmierCreateSchema,
    update_schema=InfirmierUpdateSchema,
    db_session=get_db,
    db_model=Infirmier,
    prefix='infirmier',
    page_size=10,
)

caissier_router = CRUDRouter(
    schema=CaissierSchema,
    schema_detailed=CaissierDetailedSchema,
    create_schema=CaissierCreateSchema,
    update_schema=CaissierUpdateSchema,
    db_session=get_db,
    db_model=Caissier,
    prefix='caissier',
    page_size=10,
)

compte_router = CRUDRouter(
    schema=CompteSchema,
    schema_detailed=CompteDetailedSchema,
    create_schema=CompteCreateSchema,
    update_schema=CompteUpdateSchema,
    db_session=get_db,
    db_model=Compte,
    prefix='compte',
    page_size=10,
)

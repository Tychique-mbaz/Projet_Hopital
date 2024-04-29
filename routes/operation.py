from routes.crud_router import CRUDRouter
from database.tables.operation import Reception, ActeChirurgical
from database.base import get_db
from schemas.operation import (
    ReceptionSchema,
    ReceptionDetailedSchema,
    ReceptionCreateSchema,
    ReceptionUpdateSchema,
    ActeChirurgicalSchema,
    ActeChirurgicalDetailedSchema,
    ActeChirurgicalCreateSchema,
    ActeChirurgicalUpdateSchema,
)


reception_router = CRUDRouter(
    schema=ReceptionSchema,
    schema_detailed=ReceptionDetailedSchema,
    create_schema=ReceptionCreateSchema,
    update_schema=ReceptionUpdateSchema,
    db_session=get_db,
    db_model=Reception,
    prefix="reception",
    page_size=10,
)


acte_chirurgical_router = CRUDRouter(
    schema=ActeChirurgicalSchema,
    schema_detailed=ActeChirurgicalDetailedSchema,
    create_schema=ActeChirurgicalCreateSchema,
    update_schema=ActeChirurgicalUpdateSchema,
    db_session=get_db,
    db_model=ActeChirurgical,
    prefix="acte_chirurgical",
    page_size=10,
)

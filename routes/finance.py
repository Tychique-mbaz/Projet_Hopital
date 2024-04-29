from database.tables.finance import Facture, DetailsFacture
from database.base import get_db
from schemas.finance import (
    FactureSchema,
    FactureDetailedSchema,
    FactureCreateSchema,
    FactureUpdateSchema,
    DetailsFactureSchema,
    DetailsFactureDetailedSchema,
    DetailsFactureCreateSchema,
    DetailsFactureUpdateSchema,
)
from routes.crud_router import CRUDRouter

facture_router = CRUDRouter(
    schema=FactureSchema,
    schema_detailed=FactureDetailedSchema,
    create_schema=FactureCreateSchema,
    update_schema=FactureUpdateSchema,
    db_session=get_db,
    db_model=Facture,
    prefix='facture',
    page_size=10,
)


details_facture_router = CRUDRouter(
    schema=DetailsFactureSchema,
    schema_detailed=DetailsFactureDetailedSchema,
    create_schema=DetailsFactureCreateSchema,
    update_schema=DetailsFactureUpdateSchema,
    db_session=get_db,
    db_model=DetailsFacture,
    prefix='details_facture',
    page_size=10,
)

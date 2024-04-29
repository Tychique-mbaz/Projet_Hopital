from routes.crud_router import CRUDRouter
from database.tables.pharmacie import Medicament, Stock
from database.base import get_db
from schemas.pharmacie import (
    MedicamentSchema,
    MedicamentDetailedSchema,
    MedicamentCreateSchema,
    MedicamentUpdateSchema,
    StockSchema,
    StockDetailedSchema,
    StockCreateSchema,
    StockUpdateSchema,
)


medicament_router = CRUDRouter(
    schema=MedicamentSchema,
    schema_detailed=MedicamentDetailedSchema,
    create_schema=MedicamentCreateSchema,
    update_schema=MedicamentUpdateSchema,
    db_session=get_db,
    db_model=Medicament,
    prefix="medicament",
    page_size=10,
)


stock_router = CRUDRouter(
    schema=StockSchema,
    schema_detailed=StockDetailedSchema,
    create_schema=StockCreateSchema,
    update_schema=StockUpdateSchema,
    db_session=get_db,
    db_model=Stock,
    prefix="stock",
    page_size=10,
)

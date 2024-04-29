from fastapi import FastAPI, Depends, APIRouter
from contextlib import asynccontextmanager
import uvicorn
from database.base import create_database
from routes.finance import facture_router, details_facture_router
from routes.medical import (
    fiche_consultation_router,
    ordonnance_router,
    antecedent_router,
    signe_vital_router,
    prescription_router,
    image_medical_router,
    examen_physique_router,
    service_medical_router,
    paraclinique_essentielle_router,
)
from routes.operation import reception_router, acte_chirurgical_router
from routes.patient import chambre_router, patient_router, hospitalisation_router
from routes.pharmacie import stock_router, medicament_router
from routes.utilisateur import (
    receptionniste_router,
    compte_router,
    employe_router,
    medecin_router,
    caissier_router,
    infirmier_router,
    pharmacien_router,
)
from routes.association import (
    a_chambre_infirmier_router, 
    a_acte_chirurgical_employe_router,
    a_medicament_prescription_router
)
from routes.authentication import authentication_router
from routes.authentication import get_current_active_user


@asynccontextmanager
async def on_startup(app: FastAPI):

    create_database()
    yield


#protected_router = APIRouter(dependencies=[Depends(get_current_active_user)])

protected_router = APIRouter()


api = FastAPI(lifespan=on_startup)


protected_router.include_router(facture_router)
protected_router.include_router(details_facture_router)
protected_router.include_router(fiche_consultation_router)
protected_router.include_router(ordonnance_router)
protected_router.include_router(antecedent_router)
protected_router.include_router(signe_vital_router)
protected_router.include_router(prescription_router)
protected_router.include_router(image_medical_router)
protected_router.include_router(examen_physique_router)
protected_router.include_router(service_medical_router)
protected_router.include_router(paraclinique_essentielle_router)


protected_router.include_router(reception_router)
protected_router.include_router(acte_chirurgical_router)


protected_router.include_router(chambre_router)
protected_router.include_router(patient_router)
protected_router.include_router(hospitalisation_router)


protected_router.include_router(stock_router)
protected_router.include_router(medicament_router)

protected_router.include_router(receptionniste_router)
protected_router.include_router(compte_router)
protected_router.include_router(employe_router)
protected_router.include_router(medecin_router)
protected_router.include_router(caissier_router)
protected_router.include_router(infirmier_router)
protected_router.include_router(pharmacien_router)
protected_router.include_router(compte_router)

protected_router.include_router(a_chambre_infirmier_router)
protected_router.include_router(a_acte_chirurgical_employe_router)
protected_router.include_router(a_medicament_prescription_router)


api.include_router(authentication_router)
api.include_router(protected_router)


if __name__ == "__main__":
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)

from sqlalchemy import Column, Integer, String, DateTime, Date, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.base import Base
from sqlalchemy import event
import pathlib

class Patient(Base) :

    __tablename__ = 'patient'
    id = Column(Integer, primary_key=True)
    nom = Column(String(256))
    postnom = Column(String(256))
    prenom = Column(String(256))
    adresse = Column(String(256))
    numero_telephone = Column(String(256))
    age = Column(Integer)
    poids = Column(Integer)
    sexe = Column(String(256))
    date_naissance = Column(Date)
    lieu_naissance = Column(String(256))
    profession = Column(String(256))
    etat_civil = Column(String(256))
    chemin_fichier = Column(String(1024))

    actes_chirurgicales = relationship('ActeChirurgical', back_populates='patient', cascade='all, delete-orphan')
    factures = relationship('Facture', back_populates='patient', cascade='all, delete-orphan')
    hospitalisations = relationship('Hospitalisation', back_populates='patient', cascade='all, delete-orphan')
    images_medicales = relationship('ImageMedical', back_populates='patient', cascade='all, delete-orphan')
    examens_physiques = relationship('ExamenPhysique', back_populates='patient', cascade='all, delete-orphan')
    fiches_consultations = relationship('FicheConsultation', back_populates='patient', cascade='all, delete-orphan')
    ordonnances = relationship('Ordonnance', back_populates='patient', cascade='all, delete-orphan')


# Image clean operation
@event.listens_for(Patient, 'before_delete')
def receive_before_delete(mapper, connection, target):
    "listen for the 'before_delete' event"
    for image_medical in target.images_medicales :
        pathlib.Path(image_medical.chemin_fichier).unlink(True)


class Hospitalisation(Base) :

    __tablename__ = 'hospitalisation'
    id = Column(Integer, primary_key=True)
    date_entree = Column(DateTime)
    date_sortie = Column(DateTime)
    motif = Column(Text)

    patient_id = Column(Integer, ForeignKey('patient.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    patient = relationship('Patient', back_populates='hospitalisations')

    chambre_id = Column(Integer, ForeignKey('chambre.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    chambre = relationship('Chambre', back_populates='hospitalisation')

    service_medical_id = Column(Integer, ForeignKey('service_medical.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    service_medical = relationship('ServiceMedical', back_populates='hospitalisations')


class Chambre(Base) :

    __tablename__ = 'chambre'
    id = Column(Integer, primary_key=True)
    numero_chambre = Column(Integer)
    status = Column(Boolean)            # Occupé ou libre

    hospitalisation = relationship('Hospitalisation', back_populates='chambre', uselist=False, cascade='all, delete-orphan')

    infirmiers = relationship('AssociationChambreInfirmier', back_populates='chambre')

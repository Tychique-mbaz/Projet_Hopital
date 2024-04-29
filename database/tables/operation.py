from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base 


class Reception(Base) :

    __tablename__ = 'reception'
    id = Column(Integer, primary_key=True)
    nom = Column(String(256))
    postnom = Column(String(256))
    prenom = Column(String(256))
    heure_arrive = Column(DateTime)
    recu = Column(Boolean)                  # Yes or No

    medecin_id = Column(Integer, ForeignKey('medecin.id'), nullable=True)
    medecin = relationship('Medecin', back_populates='receptions')


class ActeChirurgical(Base) :

    __tablename__ = 'acte_chirurgical'
    id = Column(Integer, primary_key=True)
    type_chirurgie = Column(String(256))
    debut = Column(DateTime)
    duree_operation = Column(Integer)
    complications_eventuelles = Column(Text)
    anesthesie_utilise = Column(String(256))

    patient_id = Column(Integer, ForeignKey('patient.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    patient = relationship('Patient', back_populates='actes_chirurgicales')

    chirurgien_principal_id = Column(Integer, ForeignKey('medecin.id'), nullable=True)
    chirurgien_principal = relationship('Medecin', back_populates='actes_chirurgicals')

    assistants = relationship('AssociationActeChirurgicalEmploye', back_populates='acte_chirurgical')

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base


class Facture(Base) :

    __tablename__ = 'facture'
    id = Column(Integer, primary_key=True)
    date_emission = Column(DateTime)
    montant_total = Column(String(100))
    type_service = Column(String(256))
    details_facture = relationship('DetailsFacture', back_populates='facture', cascade='all, delete-orphan')

    patient_id = Column(Integer, ForeignKey('patient.id'), nullable=True)
    patient = relationship('Patient', back_populates='factures')


class DetailsFacture(Base) :

    __tablename__ = 'details_facture'
    id = Column(Integer, primary_key=True)
    description = Column(String(256))
    quantite = Column(Integer)
    prix_unitaire = Column(String(256))
    facture_id = Column(Integer, ForeignKey('facture.id', onupdate='CASCADE', ondelete='CASCADE'))
    facture = relationship('Facture', back_populates='details_facture')

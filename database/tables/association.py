from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base


class AssociationChambreInfirmier(Base) :
    
    __tablename__ = 'association_chambre_infirmier'
    chambre_id = Column(Integer, ForeignKey('chambre.id'), primary_key=True)
    infirmier_id = Column(Integer, ForeignKey('infirmier.id'), primary_key=True)
    chambre = relationship('Chambre', back_populates='infirmiers')
    infirmier = relationship('Infirmier', back_populates='chambres')


class AssociationActeChirurgicalEmploye(Base) :
    
    __tablename__ = 'association_acte_chirurgical_employe'
    acte_chirurgical_id = Column(Integer, ForeignKey('acte_chirurgical.id'), primary_key=True)
    employe_id = Column(Integer, ForeignKey('employe.id'), primary_key=True)
    acte_chirurgical = relationship('ActeChirurgical', back_populates='assistants')
    employe = relationship('Employe', back_populates='actes_chirurgicals')


class AssociationMedicamentPrescription(Base) :
    
    __tablename__ = 'association_medicament_prescription'
    medicament_id = Column(Integer, ForeignKey('medicament.id'), primary_key=True)
    prescription_id = Column(Integer, ForeignKey('prescription.id'), primary_key=True)
    medicament = relationship('Medicament', back_populates='prescriptions')
    prescription = relationship('Prescription', back_populates='medicaments')





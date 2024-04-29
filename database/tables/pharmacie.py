from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base


class Medicament(Base) :

    __tablename__ = 'medicament'
    id = Column(Integer, primary_key=True)
    nom = Column(String(256))
    date_expiration = Column(Date)
    prix_unitaire = Column(String(256))

    stocks = relationship('Stock', back_populates='medicament', cascade='all, delete-orphan')
    prescriptions = relationship(
        'AssociationMedicamentPrescription',    
        back_populates='medicament'
    )


class Stock(Base) :

    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    quantite_disponible = Column(Integer)
    quantite_entree = Column(Integer)
    quantite_sortie = Column(Integer)
    date_mouvement = Column(Date)
    prix_unitaire = Column(String(256))
    
    medicament_id = Column(Integer, ForeignKey('medicament.id'))
    medicament = relationship('Medicament', back_populates='stocks')
    

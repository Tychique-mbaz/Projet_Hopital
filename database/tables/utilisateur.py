from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database.base import Base


class Employe(Base) :

    __tablename__ = 'employe'
    id = Column(Integer, primary_key=True)
    nom = Column(String(256))
    postnom = Column(String(256))
    prenom = Column(String(256))
    adresse_physique = Column(String(256))
    horaire_travail = Column(String(256))   # Avant midi, après-midi, matin; nuit...

    receptionniste = relationship('Receptionniste', back_populates='employe', uselist=False, cascade='all, delete-orphan')
    pharmacien = relationship('Pharmacien', back_populates='employe', uselist=False, cascade='all, delete-orphan')
    medecin = relationship('Medecin', back_populates='employe', uselist=False, cascade='all, delete-orphan')
    caissier = relationship('Caissier', back_populates='employe', uselist=False, cascade='all, delete-orphan')
    infirmier = relationship('Infirmier', back_populates='employe', uselist=False, cascade='all, delete-orphan')
    compte = relationship('Compte', back_populates='employe', uselist=False, cascade='all, delete-orphan')

    actes_chirurgicals = relationship('AssociationActeChirurgicalEmploye', back_populates='employe')


class Medecin(Base) :

    __tablename__ = 'medecin'
    id = Column(Integer, primary_key=True)
    specialisation = Column(String(256))

    employe_id = Column(Integer, ForeignKey('employe.id', onupdate='CASCADE', ondelete='CASCADE'))
    employe = relationship('Employe', back_populates='medecin')
    fiches_consultations = relationship('FicheConsultation', back_populates='medecin')
    receptions = relationship('Reception', back_populates='medecin')
    actes_chirurgicals = relationship('ActeChirurgical', back_populates='chirurgien_principal')


class Receptionniste(Base) :
    
    __tablename__ = 'receptionniste'
    id = Column(Integer, primary_key=True)
    
    employe_id = Column(Integer, ForeignKey('employe.id', onupdate='CASCADE', ondelete='CASCADE'))
    employe = relationship('Employe', back_populates='receptionniste')


class Pharmacien(Base) :
    
    __tablename__ = 'pharmacien'
    id = Column(Integer, primary_key=True)

    employe_id = Column(Integer, ForeignKey('employe.id', onupdate='CASCADE', ondelete='CASCADE'))
    employe = relationship('Employe', back_populates='pharmacien')
    

class Infirmier(Base) :
    
    __tablename__ = 'infirmier'
    id = Column(Integer, primary_key=True)

    employe_id = Column(Integer, ForeignKey('employe.id', onupdate='CASCADE', ondelete='CASCADE'))
    employe = relationship('Employe', back_populates='infirmier')

    chambres = relationship('AssociationChambreInfirmier', back_populates='infirmier')


class Caissier(Base) :
    
    __tablename__ = 'caissier'
    id = Column(Integer, primary_key=True)
    numero_caisse = Column(Integer)

    employe_id = Column(Integer, ForeignKey('employe.id', onupdate='CASCADE', ondelete='CASCADE'))
    employe = relationship('Employe', back_populates='caissier')


class Compte(Base) :
    
    __tablename__ = 'compte'
    id = Column(Integer, primary_key=True)
    username = Column(String(256))
    passeword = Column(String(256))
    date_derniere_connexion = Column(DateTime)
    email = Column(String(256))
    role = Column(String(256))
    status = Column(String(256))                # actif, inactif, bloqué
    disabled = Column(Boolean, default=False)

    employe_id = Column(Integer, ForeignKey('employe.id', onupdate='CASCADE', ondelete='CASCADE'))
    employe = relationship('Employe', back_populates='compte')

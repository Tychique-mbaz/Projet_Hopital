from sqlalchemy import Column, Integer, String, DateTime, Date, Text, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base


class Ordonnance(Base) :
    
    __tablename__ = 'ordonnance'
    id = Column(Integer, primary_key=True)
    date_emission = Column(DateTime)
    designation = Column(Text)
    indications = Column(Text)
    patient_id = Column(Integer, ForeignKey('patient.id', onupdate='CASCADE', ondelete='CASCADE'))
    patient = relationship('Patient', back_populates='ordonnances')


class FicheConsultation(Base) :

    __tablename__ = 'fiche_consultation'
    id = Column(Integer, primary_key=True)
    motif_consultation = Column(Text)
    etat_vaccinal = Column(Text)                          # Rhume, toux
    prise_charge_medical_et_psychosociale = Column(Text)
    date_emission = Column(DateTime)

    patient_id = Column(Integer, ForeignKey('patient.id', onupdate='CASCADE', ondelete='CASCADE'))
    patient = relationship('Patient', back_populates='fiches_consultations')
    
    medecin_id = Column(Integer, ForeignKey('medecin.id'), nullable=True)
    medecin = relationship('Medecin', back_populates='fiches_consultations')
    
    prescriptions = relationship('Prescription', back_populates='fiche_consultation', cascade='all, delete-orphan')
    antecedents = relationship('Antecedent', back_populates='fiche_consultation', cascade='all, delete-orphan')
    signes_vitaux = relationship('SigneVital', back_populates='fiche_consultation', cascade='all, delete-orphan')
    examens_physiques = relationship('ExamenPhysique', back_populates='fiche_consultation', cascade='all, delete-orphan')
    paracliniques_essentielles = relationship('ParacliniqueEssentielle', back_populates='fiche_consultation', cascade='all, delete-orphan')



class Prescription(Base) :

    __tablename__ = 'prescription'
    id = Column(Integer, primary_key=True)
    posologie = Column(Text)
    date_prescription = Column(Date)
    quantite = Column(Integer)

    fiche_consultation_id = Column(Integer, ForeignKey('fiche_consultation.id', onupdate='CASCADE', ondelete='CASCADE'))
    fiche_consultation = relationship('FicheConsultation', back_populates='prescriptions')

    medicaments = relationship('AssociationMedicamentPrescription', back_populates='prescription')


class Antecedent(Base) :

    __tablename__ = 'antecedent'
    id = Column(Integer, primary_key=True)
    question = Column(String(256))
    reponse = Column(Text)

    fiche_consultation_id = Column(Integer, ForeignKey('fiche_consultation.id', onupdate='CASCADE', ondelete='CASCADE'))
    fiche_consultation = relationship('FicheConsultation', back_populates='antecedents')



class SigneVital(Base) :

    __tablename__ = 'signe_vital'
    id = Column(Integer, primary_key=True)
    nom_signe = Column(String(256))        # Pouls, Fr, glycémie
    valeur = Column(String(256))
    date_heure_mesure = Column(DateTime)

    fiche_consultation_id = Column(Integer, ForeignKey('fiche_consultation.id', onupdate='CASCADE', ondelete='CASCADE'))
    fiche_consultation = relationship('FicheConsultation', back_populates='signes_vitaux')



class ExamenPhysique(Base) :
    
    __tablename__ = 'examen_physique'
    id = Column(Integer, primary_key=True)
    type_examen = Column(String(256))
    resultat = Column(String(256))
    date_realisation = Column(DateTime)

    fiche_consultation_id = Column(Integer, ForeignKey('fiche_consultation.id'), nullable=True)
    fiche_consultation = relationship('FicheConsultation', back_populates='examens_physiques')

    patient_id = Column(Integer, ForeignKey('patient.id'), nullable=True)
    patient = relationship('Patient', back_populates='examens_physiques')


    
class ServiceMedical(Base) :
    
    __tablename__ = 'service_medical'
    id = Column(Integer, primary_key=True)
    nom_service = Column(String(256))      # Néonatalité, Medecine interne (Homme & Femme)
    
    hospitalisations = relationship('Hospitalisation', back_populates='service_medical')



class ImageMedical(Base) :
    
    __tablename__ = 'image_medical'
    id = Column(Integer, primary_key=True)
    type_image = Column(String(256))       # IRM, radiographie, échographie
    date_prise = Column(DateTime)
    chemin_fichier = Column(String(1024))

    patient_id = Column(Integer, ForeignKey('patient.id', onupdate='CASCADE', ondelete='CASCADE'), nullable=True)
    patient = relationship('Patient', back_populates='images_medicales')

    paraclinique_essentielle = relationship('ParacliniqueEssentielle', back_populates='image_medical', uselist=False)
    

class ParacliniqueEssentielle(Base) :
    
    __tablename__ = 'paraclinique_essentielle'
    id = Column(Integer, primary_key=True)
    intitule = Column(String(256))
    reponse = Column(String(256))

    fiche_consultation_id = Column(Integer, ForeignKey('fiche_consultation.id'), nullable=True)
    fiche_consultation = relationship('FicheConsultation', back_populates='paracliniques_essentielles')

    image_medical_id = Column(Integer, ForeignKey('image_medical.id'), nullable=True)
    image_medical = relationship('ImageMedical', back_populates='paraclinique_essentielle')

    

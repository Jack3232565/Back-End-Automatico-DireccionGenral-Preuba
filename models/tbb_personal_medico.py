from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Float
from sqlalchemy.orm import relationship
from config.db import Base
import enum

class Tipo(str, enum.Enum):
    Medico = 'Medico'
    Enfermero = 'Enfermero'
    Administrativo = 'Administrativo'
    Directivo = 'Directivo'
    Apoyo = 'Apoyo'
    Residente = 'Residente'
    Interno = 'Interno'

class Estatus(str, enum.Enum):
    Activo = 'Activo'
    Inactivo = 'Inactivo'

class TbbPersonalMedico(Base):
    __tablename__ = 'tbb_personal_medico'   

    Persona_ID = Column(Integer, primary_key=True, index=True)
    Departamento_ID = Column(Integer, ForeignKey('tbc_departamentos.id'))
    Cedula_Profesional = Column(String(25), index=True)
    Tipo = Column(Enum(Tipo))
    Especialidad = Column(String(25), nullable=True)
    Fecha_Registro = Column(DateTime)
    Fecha_Contratacion = Column(DateTime)
    Fecha_Termino_Contrato = Column(DateTime, nullable=True)
    Salario = Column(Float)
    Estatus = Column(Enum(Estatus)) 

    departamento = relationship("Departamento", back_populates="personal_medico")
    
    solicitudes = relationship("TbdSolicitudes", back_populates="personal_medico")

    aprobaciones = relationship("Aprobaciones", back_populates="personal_medico")
    
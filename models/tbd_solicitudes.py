from sqlalchemy import Column, Integer, ForeignKey, Enum, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from config.db import Base
import enum

class Prioridad(enum.Enum):
    Urgente = 'Urgente'
    Alta = 'Alta'
    Moderada = 'Moderada'
    Emergente = 'Emergente'
    Normal = 'Normal'

class Estatus(enum.Enum):
    Registrada = 'Registrada'
    Programada = 'Programada'
    Cancelada = 'Cancelada'
    Reprogramada = 'Reprogramada'
    En_Proceso = 'En Proceso'
    Realizada = 'Realizada'

class TbdSolicitudes(Base):
    __tablename__ = "tbd_solicitudes"

    ID = Column(Integer, primary_key=True, index=True)
    Paciente_ID = Column(Integer, ForeignKey("tbb_pacientes.Persona_ID"), nullable=False)
    Medico_ID = Column(Integer, ForeignKey("tbb_personal_medico.Persona_ID"), nullable=False)
    Servicio_ID = Column(Integer, ForeignKey("tbc_servicios_medicos.ID"), nullable=False)
    Prioridad = Column(Enum(Prioridad), nullable=False)
    Descripcion = Column(Text, nullable=False)
    Estatus = Column(Enum(Estatus), nullable=False, default=Estatus.En_Proceso)
    Estatus_Aprobacion = Column(Boolean, nullable=False, default=False)
    Fecha_Registro = Column(DateTime, default=datetime.utcnow, nullable=False)
    Fecha_Actualizacion = Column(DateTime, nullable=True)

    paciente = relationship("TbbPacientes", back_populates="solicitudes")
    servicio_medico = relationship("ServicioMedico", back_populates="solicitudes")
    personal_medico = relationship("TbbPersonalMedico", back_populates="solicitudes")

    aprobaciones = relationship("Aprobaciones", back_populates="solicitudes")



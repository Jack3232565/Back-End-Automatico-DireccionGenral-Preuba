from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import enum

class Prioridad(str, enum.Enum):
    Urgente = 'Urgente'
    Alta = 'Alta'
    Moderada = 'Moderada'
    Emergente = 'Emergente'
    Normal = 'Normal'

class Estatus1(str, enum.Enum):
    Registrada = 'Registrada'
    Programada = 'Programada'
    Cancelada = 'Cancelada'
    Reprogramada = 'Reprogramada'
    En_Proceso = 'En Proceso'
    Realizada = 'Realizada'

class TbdSolicitudesBase(BaseModel):
    Paciente_ID: int
    Medico_ID: int
    Servicio_ID: int
    Prioridad: Prioridad
    Descripcion: str
    Estatus: Estatus1 = Estatus1.Registrada
    Estatus_Aprobacion: bool = False
    Fecha_Registro: datetime = Field(default_factory=datetime.utcnow)
    Fecha_Actualizacion: Optional[datetime] = None

class TbdSolicitudesCreate(TbdSolicitudesBase):
    pass

class TbdSolicitudesUpdate(TbdSolicitudesBase):
    pass

class TbdSolicitudes(TbdSolicitudesBase):
    ID: int

    class Config:
        from_attributes = True
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
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

class TbbPersonalMedicoBase(BaseModel):
    Departamento_ID: int
    Cedula_Profesional: str
    Tipo: Tipo
    Especialidad: Optional[str] = None
    Fecha_Registro: datetime
    Fecha_Contratacion: datetime
    Fecha_Termino_Contrato: Optional[datetime] = None
    Salario: float
    Estatus: Estatus

class TbbPersonalMedicoCreate(TbbPersonalMedicoBase):
    pass

class TbbPersonalMedicoUpdate(TbbPersonalMedicoBase):
    pass

class TbbPersonalMedico(TbbPersonalMedicoBase):
    
    Persona_ID: int
from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class AreasMedicasBase(BaseModel):
    Nombre: str
    Descripcion: str
    Estatus: str
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

    class Config:
        from_attributes = True

class AreasMedicasBaseCreate(AreasMedicasBase):
    pass

class AreasMedicasBaseUpdate(AreasMedicasBase):
    pass

class AreasMedicas(AreasMedicasBase):
    id: int

# from sqlalchemy import Column, Integer, String, Enum, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from datetime import datetime
# from enum import Enum as PyEnum

# Base = declarative_base()

# class EstadoEnum(PyEnum):
#     Activo = "Activo"
#     Inactivo = "Inactivo"

# class TbcAreasMedica(Base):
#     __tablename__ = 'tbc_areas_medicas'

#     id = Column(Integer, primary_key=True, index=True)
#     Nombre = Column(String(50), index=True)  # Especifica una longitud para VARCHAR
#     Descripcion = Column(String(255))  # Especifica una longitud para VARCHAR
#     Estatus = Column(Enum(EstadoEnum))  # Usa el Enum definido
#     Fecha_Registro = Column(DateTime, default=datetime.utcnow)
#     Fecha_Actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from enum import Enum as PyEnum
from config.db import Base


class EstadoEnum(PyEnum):
    Activo = "Activo"
    Inactivo = "Inactivo"

class TbcAreasMedica(Base):
    __tablename__ = 'tbc_areas_medicas'

    id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(50), index=True)
    Descripcion = Column(String(255))
    Estatus = Column(Enum(EstadoEnum))
    Fecha_Registro = Column(DateTime, default=datetime.utcnow)
    Fecha_Actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    departamentos = relationship("Departamento", back_populates="area_medica")
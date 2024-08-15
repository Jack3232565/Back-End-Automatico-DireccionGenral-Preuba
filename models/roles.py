from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, func
from config.db import Base
from sqlalchemy.orm import relationship


class Roles(Base):
    __tablename__ = 'tbc_roles'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    Nombre = Column(String(50), nullable=False)
    Descripcion = Column(Text)
    Estatus = Column(Boolean, default=True)
    Fecha_Registro = Column(DateTime, nullable=False, server_default=func.now())
    Fecha_Actualizacion = Column(DateTime, onupdate=func.now())


    usuarios = relationship("UsuarioRoles", back_populates="rol")
    
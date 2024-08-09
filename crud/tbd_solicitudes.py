from sqlalchemy.orm import Session
from models.tbd_solicitudes import TbdSolicitudes
from schemas.tbd_solicitudes import TbdSolicitudesCreate, TbdSolicitudesUpdate

def create_solicitud(db: Session, solicitud: TbdSolicitudesCreate) -> TbdSolicitudes:
    # Crear una nueva instancia de TbdSolicitudes a partir del esquema
    db_solicitud = TbdSolicitudes(
        Paciente_ID=solicitud.Paciente_ID,
        Medico_ID=solicitud.Medico_ID,
        Servicio_ID=solicitud.Servicio_ID,
        Prioridad=solicitud.Prioridad,
        Descripcion=solicitud.Descripcion,
        Estatus=solicitud.Estatus,
        Estatus_Aprobacion=solicitud.Estatus_Aprobacion,
        Fecha_Registro=solicitud.Fecha_Registro,
        Fecha_Actualizacion=solicitud.Fecha_Actualizacion,
    )
    db.add(db_solicitud)
    db.commit()
    db.refresh(db_solicitud)
    return db_solicitud

def get_solicitud(db: Session, solicitud_id: int) -> TbdSolicitudes:
    # Obtener una solicitud por ID
    return db.query(TbdSolicitudes).filter(TbdSolicitudes.ID == solicitud_id).first()

def get_solicitudes(db: Session, skip: int = 0, limit: int = 10) -> list[TbdSolicitudes]:
    # Obtener una lista de solicitudes con paginación
    return db.query(TbdSolicitudes).offset(skip).limit(limit).all()

def update_solicitud(db: Session, solicitud_id: int, solicitud: TbdSolicitudesUpdate) -> TbdSolicitudes:
    # Actualizar una solicitud existente
    db_solicitud = db.query(TbdSolicitudes).filter(TbdSolicitudes.ID == solicitud_id).first()
    if db_solicitud:
        for key, value in solicitud.dict(exclude_unset=True).items():
            setattr(db_solicitud, key, value)
        db.commit()
        db.refresh(db_solicitud)
    return db_solicitud

def delete_solicitud(db: Session, solicitud_id: int) -> TbdSolicitudes:
    # Eliminar una solicitud existente
    db_solicitud = db.query(TbdSolicitudes).filter(TbdSolicitudes.ID == solicitud_id).first()
    if db_solicitud:
        db.delete(db_solicitud)
        db.commit()
    return db_solicitud

def get_solicitudes_by_params(
    db: Session,
    paciente_id: int = None,
    medico_id: int = None,
    servicio_id: int = None,
    skip: int = 0,
    limit: int = 10
) -> list[TbdSolicitudes]:
    # Obtener solicitudes basadas en múltiples parámetros opcionales
    query = db.query(TbdSolicitudes)
    if paciente_id is not None:
        query = query.filter(TbdSolicitudes.Paciente_ID == paciente_id)
    if medico_id is not None:
        query = query.filter(TbdSolicitudes.Medico_ID == medico_id)
    if servicio_id is not None:
        query = query.filter(TbdSolicitudes.Servicio_ID == servicio_id)
    return query.offset(skip).limit(limit).all()

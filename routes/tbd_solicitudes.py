from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import crud.tbd_solicitudes, config.db, schemas.tbd_solicitudes, models.tbd_solicitudes

# Crear el enrutador para las solicitudes
tbd_solicitudes_router = APIRouter(tags=["Tbd_Solicitudes"])

# Crear la base de datos (si no existe)
models.tbd_solicitudes.Base.metadata.create_all(bind=config.db.engine)

# Función para obtener una sesión de base de datos
def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear una nueva solicitud
@tbd_solicitudes_router.post("/tbd_solicitudes/", response_model=schemas.tbd_solicitudes.TbdSolicitudes)
def create_solicitud(solicitud: schemas.tbd_solicitudes.TbdSolicitudesCreate, db: Session = Depends(get_db)):
    # Verificar si ya existe una solicitud con los mismos parámetros
    existing_solicitudes = crud.tbd_solicitudes.get_solicitudes_by_params(
        db=db,
        paciente_id=solicitud.Paciente_ID,
        medico_id=solicitud.Medico_ID,
        servicio_id=solicitud.Servicio_ID
    )
    if existing_solicitudes:
        raise HTTPException(status_code=400, detail="Solicitud ya existe con los mismos parámetros")
    return crud.tbd_solicitudes.create_solicitud(db, solicitud)

# Ruta para obtener una solicitud por ID
@tbd_solicitudes_router.get("/tbd_solicitudes/{id}", response_model=schemas.tbd_solicitudes.TbdSolicitudes)
def read_solicitud(id: int, db: Session = Depends(get_db)):
    db_solicitud = crud.tbd_solicitudes.get_solicitud(db, id)
    if db_solicitud is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return db_solicitud

# Ruta para obtener todas las solicitudes con paginación
@tbd_solicitudes_router.get("/tbd_solicitudes/", response_model=List[schemas.tbd_solicitudes.TbdSolicitudes])
def read_solicitudes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.tbd_solicitudes.get_solicitudes(db, skip=skip, limit=limit)

# Ruta para actualizar una solicitud por ID
@tbd_solicitudes_router.put("/tbd_solicitudes/{id}", response_model=schemas.tbd_solicitudes.TbdSolicitudes)
def update_solicitud(id: int, solicitud: schemas.tbd_solicitudes.TbdSolicitudesUpdate, db: Session = Depends(get_db)):
    db_solicitud = crud.tbd_solicitudes.get_solicitud(db, id)
    if db_solicitud is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return crud.tbd_solicitudes.update_solicitud(db, id, solicitud)

# Ruta para eliminar una solicitud por ID
@tbd_solicitudes_router.delete("/tbd_solicitudes/{id}", response_model=schemas.tbd_solicitudes.TbdSolicitudes)
def delete_solicitud(id: int, db: Session = Depends(get_db)):
    db_solicitud = crud.tbd_solicitudes.get_solicitud(db, id)
    if db_solicitud is None:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return crud.tbd_solicitudes.delete_solicitud(db, id)

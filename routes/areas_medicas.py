from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import crud.areas_medicas as crud
import config.db as config
import schemas.areas_medicas as schemas
import models.areas_medicas as models
from typing import List
from cryptography.fernet import Fernet
from portadortoken import Portador

key = Fernet.generate_key()
f = Fernet(key)

areas_medicas = APIRouter()

models.Base.metadata.create_all(bind=config.engine)

def get_db():
    db = config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@areas_medicas.get("/areas_medicas/", response_model=List[schemas.AreasMedicasBase], tags=["Tbc_Areas_Medicas"], dependencies=[Depends(Portador())])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_areasmedicass = crud.get_all_areas(db=db, skip=skip, limit=limit)
    return db_areasmedicass

@areas_medicas.get("/areas_medicas/{id}", response_model=schemas.AreasMedicasBase, tags=["Tbc_Areas_Medicas"], dependencies=[Depends(Portador())])
def read_role(id: int, db: Session = Depends(get_db)):
    db_areasmedicas = crud.get_areas(db=db, id=id)
    if db_areasmedicas is None:
        raise HTTPException(status_code=404, detail="Area Medica No Encontrada")
    return db_areasmedicas

@areas_medicas.post("/areas_medicas/", response_model=schemas.AreasMedicasBase, tags=["Tbc_Areas_Medicas"], dependencies=[Depends(Portador())])
def create_areas(areas: schemas.AreasMedicasBaseCreate, db: Session = Depends(get_db)):
    db_areasmedicas = crud.get_areas_by_name(db, nombre=areas.Nombre)
    if db_areasmedicas:
        raise HTTPException(status_code=400, detail="Rol existente, intenta nuevamente")
    return crud.create_areas(db=db, areas=areas)

@areas_medicas.put("/areas_medicas/{id}", response_model=schemas.AreasMedicasBase, tags=["Tbc_Areas_Medicas"], dependencies=[Depends(Portador())])
def update_areas(id: int, areas: schemas.AreasMedicasBaseUpdate, db: Session = Depends(get_db)):
    db_areasmedicas = crud.update_areas(db=db, id=id, areas=areas)
    if db_areasmedicas is None:
        raise HTTPException(status_code=404, detail="Area Medica no existe, no actualizado")
    return db_areasmedicas

@areas_medicas.delete("/areas_medicas/{id}", response_model=schemas.AreasMedicasBase, tags=["Tbc_Areas_Medicas"], dependencies=[Depends(Portador())])
def delete_areas(id: int, db: Session = Depends(get_db)):
    db_areasmedicas = crud.delete_areas(db=db, id=id)
    if db_areasmedicas is None:
        raise HTTPException(status_code=404, detail="Area Medica no existe, no se pudo eliminar")
    return db_areasmedicas
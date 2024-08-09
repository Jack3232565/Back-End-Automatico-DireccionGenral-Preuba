from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.tbb_personal_medico import TbbPersonalMedico, TbbPersonalMedicoCreate, TbbPersonalMedicoUpdate
from crud.tbb_personal_medico import create_personal_medico, get_personal_medico, get_personal_medico_list, update_personal_medico, delete_personal_medico
import config.db as db_config
import models.tbb_personal_medico

personal_medico = APIRouter(tags=["Tbb_Personal_Medico"])

models.tbb_personal_medico.Base.metadata.create_all(bind=db_config.engine)

def get_db():
    db = db_config.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@personal_medico.post("/personal-medico/", response_model=TbbPersonalMedico)
def create_personal_medico_endpoint(personal_medico: TbbPersonalMedicoCreate, db: Session = Depends(get_db)):
    return create_personal_medico(db=db, personal_medico=personal_medico)

@personal_medico.get("/personal-medico/{persona_id}", response_model=TbbPersonalMedico)
def read_personal_medico(persona_id: int, db: Session = Depends(get_db)):
    db_personal_medico = get_personal_medico(db, persona_id)
    if db_personal_medico is None:
        raise HTTPException(status_code=404, detail="Personal Medico not found")
    return db_personal_medico

@personal_medico.get("/personal-medico/", response_model=List[TbbPersonalMedico])
def read_personal_medico_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_personal_medico_list(db, skip=skip, limit=limit)

@personal_medico.put("/personal-medico/{persona_id}", response_model=TbbPersonalMedico)
def update_personal_medico_endpoint(persona_id: int, personal_medico: TbbPersonalMedicoUpdate, db: Session = Depends(get_db)):
    db_personal_medico = update_personal_medico(db, persona_id, personal_medico)
    if db_personal_medico is None:
        raise HTTPException(status_code=404, detail="Personal Medico not found")
    return db_personal_medico

@personal_medico.delete("/personal-medico/{persona_id}", response_model=TbbPersonalMedico)
def delete_personal_medico_endpoint(persona_id: int, db: Session = Depends(get_db)):
    db_personal_medico = delete_personal_medico(db, persona_id)
    if db_personal_medico is None:
        raise HTTPException(status_code=404, detail="Personal Medico not found")
    return db_personal_medico
from sqlalchemy.orm import Session
from models.areas_medicas import TbcAreasMedica
from schemas.areas_medicas import AreasMedicasBaseCreate, AreasMedicasBaseUpdate

def get_all_areas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TbcAreasMedica).offset(skip).limit(limit).all()

def get_areas(db: Session, id: int):
    return db.query(TbcAreasMedica).filter(TbcAreasMedica.id == id).first()

def get_areas_by_name(db: Session, nombre: str):
    return db.query(TbcAreasMedica).filter(TbcAreasMedica.Nombre == nombre).first()

def create_areas(db: Session, areas: AreasMedicasBaseCreate):
    db_areas = TbcAreasMedica(**areas.dict())
    db.add(db_areas)
    db.commit()
    db.refresh(db_areas)
    return db_areas

def update_areas(db: Session, id: int, areas: AreasMedicasBaseUpdate):
    db_areas = get_areas(db, id)
    if db_areas:
        for key, value in areas.dict().items():
            setattr(db_areas, key, value)
        db.commit()
        db.refresh(db_areas)
    return db_areas

def delete_areas(db: Session, id: int):
    db_areas = get_areas(db, id)
    if db_areas:
        db.delete(db_areas)
        db.commit()
    return db_areas
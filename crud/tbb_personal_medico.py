from sqlalchemy.orm import Session
from models.tbb_personal_medico import TbbPersonalMedico as TbbPersonalMedicoModel
from schemas.tbb_personal_medico import TbbPersonalMedicoCreate, TbbPersonalMedicoUpdate

def create_personal_medico(db: Session, personal_medico: TbbPersonalMedicoCreate):
    db_personal_medico = TbbPersonalMedicoModel(
        Departamento_ID=personal_medico.Departamento_ID,
        Cedula_Profesional=personal_medico.Cedula_Profesional,
        Tipo=personal_medico.Tipo,
        Especialidad=personal_medico.Especialidad,
        Fecha_Registro=personal_medico.Fecha_Registro,
        Fecha_Contratacion=personal_medico.Fecha_Contratacion,
        Fecha_Termino_Contrato=personal_medico.Fecha_Termino_Contrato,
        Salario=personal_medico.Salario,
        Estatus=personal_medico.Estatus
    )
    db.add(db_personal_medico)
    db.commit()
    db.refresh(db_personal_medico)
    return db_personal_medico

def get_personal_medico(db: Session, persona_id: int):
    return db.query(TbbPersonalMedicoModel).filter(TbbPersonalMedicoModel.Persona_ID == persona_id).first()

def get_personal_medico_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TbbPersonalMedicoModel).offset(skip).limit(limit).all()

def update_personal_medico(db: Session, persona_id: int, personal_medico: TbbPersonalMedicoUpdate):
    db_personal_medico = db.query(TbbPersonalMedicoModel).filter(TbbPersonalMedicoModel.Persona_ID == persona_id).first()
    if db_personal_medico is None:
        return None

    for var, value in vars(personal_medico).items():
        setattr(db_personal_medico, var, value) if value else None

    db.add(db_personal_medico)
    db.commit()
    db.refresh(db_personal_medico)
    return db_personal_medico

def delete_personal_medico(db: Session, persona_id: int):
    db_personal_medico = db.query(TbbPersonalMedicoModel).filter(TbbPersonalMedicoModel.Persona_ID == persona_id).first()
    if db_personal_medico is None:
        return None

    db.delete(db_personal_medico)
    db.commit()
    return db_personal_medico
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.funnel import Funnel as DBFunnel
from schemas.funnel import Funnel, FunnelCreate, FunnelUpdate

router = APIRouter(prefix="/funnels", tags=["funnels"])

@router.post("/", response_model=Funnel)
def create_funnel(funnel: FunnelCreate, db: Session = Depends(get_db)):
    new_funnel = DBFunnel(**funnel.dict())
    db.add(new_funnel)
    db.commit()
    db.refresh(new_funnel)
    return new_funnel

@router.get("/", response_model=list[Funnel])
def read_funnels(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    funnels = db.query(DBFunnel).offset(skip).limit(limit).all()
    return funnels

@router.get("/{funnel_id}", response_model=Funnel)
def read_funnel(funnel_id: int, db: Session = Depends(get_db)):
    funnel = db.query(DBFunnel).filter(DBFunnel.id == funnel_id).first()
    if not funnel:
        raise HTTPException(status_code=404, detail="Funnel not found")
    return funnel

@router.put("/{funnel_id}", response_model=Funnel)
def update_funnel(funnel_id: int, funnel: FunnelUpdate, db: Session = Depends(get_db)):
    db_funnel = db.query(DBFunnel).filter(DBFunnel.id == funnel_id).first()
    if db_funnel is None:
        raise HTTPException(status_code=404, detail="Funnel not found")
    for key, value in funnel.dict(exclude_unset=True).items():
        setattr(db_funnel, key, value)
    db.commit()
    db.refresh(db_funnel)
    return db_funnel

@router.delete("/{funnel_id}")
def delete_funnel(funnel_id: int, db: Session = Depends(get_db)):
    db_funnel = db.query(DBFunnel).filter(DBFunnel.id == funnel_id).first()
    if db_funnel is None:
        raise HTTPException(status_code=404, detail="Funnel not found")
    db.delete(db_funnel)
    db.commit()
    return {"message": "Funnel deleted"}

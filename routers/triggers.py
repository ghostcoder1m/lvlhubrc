from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.trigger import Trigger as DBTrigger
from schemas.trigger import Trigger, TriggerCreate, TriggerUpdate

router = APIRouter(prefix="/triggers", tags=["triggers"])

@router.post("/", response_model=Trigger)
def create_trigger(trigger: TriggerCreate, db: Session = Depends(get_db)):
    new_trigger = DBTrigger(**trigger.dict())
    db.add(new_trigger)
    db.commit()
    db.refresh(new_trigger)
    return new_trigger

@router.get("/", response_model=list[Trigger])
def get_triggers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    triggers = db.query(DBTrigger).offset(skip).limit(limit).all()
    return triggers

@router.get("/{trigger_id}", response_model=Trigger)
def get_trigger(trigger_id: int, db: Session = Depends(get_db)):
    trigger = db.query(DBTrigger).filter(DBTrigger.id == trigger_id).first()
    if not trigger:
        raise HTTPException(status_code=404, detail="Trigger not found")
    return trigger

@router.put("/{trigger_id}", response_model=Trigger)
def update_trigger(trigger_id: int, trigger_update: TriggerUpdate, db: Session = Depends(get_db)):
    trigger = db.query(DBTrigger).filter(DBTrigger.id == trigger_id).first()
    if not trigger:
        raise HTTPException(status_code=404, detail="Trigger not found")
    for key, value in trigger_update.dict(exclude_unset=True).items():
        setattr(trigger, key, value)
    db.commit()
    db.refresh(trigger)
    return trigger

@router.delete("/{trigger_id}")
def delete_trigger(trigger_id: int, db: Session = Depends(get_db)):
    trigger = db.query(DBTrigger).filter(DBTrigger.id == trigger_id).first()
    if not trigger:
        raise HTTPException(status_code=404, detail="Trigger not found")
    db.delete(trigger)
    db.commit()
    return {"message": "Trigger deleted"}

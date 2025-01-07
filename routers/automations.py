from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.automation import Automation as DBAutomation
from schemas.automation import Automation, AutomationCreate, AutomationUpdate

router = APIRouter(prefix="/automations", tags=["automations"])

@router.post("/", response_model=Automation)
def create_automation(automation: AutomationCreate, db: Session = Depends(get_db)):
    new_automation = DBAutomation(**automation.dict())
    db.add(new_automation)
    db.commit()
    db.refresh(new_automation)
    return new_automation

@router.get("/", response_model=list[Automation])
def read_automations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    automations = db.query(DBAutomation).offset(skip).limit(limit).all()
    return automations

@router.get("/{automation_id}", response_model=Automation)
def read_automation(automation_id: int, db: Session = Depends(get_db)):
    automation = db.query(DBAutomation).filter(DBAutomation.id == automation_id).first()
    if not automation:
        raise HTTPException(status_code=404, detail="Automation not found")
    return automation

@router.put("/{automation_id}", response_model=Automation)
def update_automation(automation_id: int, automation: AutomationUpdate, db: Session = Depends(get_db)):
    db_automation = db.query(DBAutomation).filter(DBAutomation.id == automation_id).first()
    if db_automation is None:
        raise HTTPException(status_code=404, detail="Automation not found")
    for key, value in automation.dict(exclude_unset=True).items():
        setattr(db_automation, key, value)
    db.commit()
    db.refresh(db_automation)
    return db_automation

@router.delete("/{automation_id}")
def delete_automation(automation_id: int, db: Session = Depends(get_db)):
    db_automation = db.query(DBAutomation).filter(DBAutomation.id == automation_id).first()
    if db_automation is None:
        raise HTTPException(status_code=404, detail="Automation not found")
    db.delete(db_automation)
    db.commit()
    return {"message": "Automation deleted"}

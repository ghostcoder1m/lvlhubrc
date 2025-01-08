from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.lead import Lead as DBLead
from schemas.lead import Lead, LeadCreate, LeadUpdate

router = APIRouter(prefix="/leads", tags=["leads"])

@router.post("/", response_model=Lead)
def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    existing_lead = db.query(DBLead).filter(DBLead.email == lead.email).first()
    if existing_lead:
        raise HTTPException(status_code=400, detail="A lead with this email already exists.")
    new_lead = DBLead(**lead.dict())
    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)
    return new_lead

@router.get("/", response_model=list[Lead])
def get_leads(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    leads = db.query(DBLead).offset(skip).limit(limit).all()
    return leads

@router.get("/{lead_id}", response_model=Lead)
def get_lead(lead_id: int, db: Session = Depends(get_db)):
    lead = db.query(DBLead).filter(DBLead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

@router.put("/{lead_id}", response_model=Lead)
def update_lead(lead_id: int, lead_update: LeadUpdate, db: Session = Depends(get_db)):
    lead = db.query(DBLead).filter(DBLead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    for key, value in lead_update.dict(exclude_unset=True).items():
        setattr(lead, key, value)
    db.commit()
    db.refresh(lead)
    return lead

@router.delete("/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(get_db)):
    lead = db.query(DBLead).filter(DBLead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    db.delete(lead)
    db.commit()
    return {"message": "Lead deleted"}

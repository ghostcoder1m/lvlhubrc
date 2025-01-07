from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.onboarding import Onboarding as DBOnboarding
from schemas.onboarding import Onboarding, OnboardingCreate, OnboardingUpdate

router = APIRouter(prefix="/onboarding", tags=["onboarding"])

@router.post("/", response_model=Onboarding)
def create_onboarding(onboarding: OnboardingCreate, db: Session = Depends(get_db)):
    new_onboarding = DBOnboarding(**onboarding.dict())
    db.add(new_onboarding)
    db.commit()
    db.refresh(new_onboarding)
    return new_onboarding

@router.get("/", response_model=list[Onboarding])
def read_onboardings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    onboardings = db.query(DBOnboarding).offset(skip).limit(limit).all()
    return onboardings

@router.get("/{onboarding_id}", response_model=Onboarding)
def read_onboarding(onboarding_id: int, db: Session = Depends(get_db)):
    db_onboarding = db.query(DBOnboarding).filter(DBOnboarding.id == onboarding_id).first()
    if db_onboarding is None:
        raise HTTPException(status_code=404, detail="Onboarding not found")
    return db_onboarding

@router.put("/{onboarding_id}", response_model=Onboarding)
def update_onboarding(onboarding_id: int, onboarding: OnboardingUpdate, db: Session = Depends(get_db)):
    db_onboarding = db.query(DBOnboarding).filter(DBOnboarding.id == onboarding_id).first()
    if db_onboarding is None:
        raise HTTPException(status_code=404, detail="Onboarding not found")
    for key, value in onboarding.dict(exclude_unset=True).items():
        setattr(db_onboarding, key, value)
    db.commit()
    db.refresh(db_onboarding)
    return db_onboarding

@router.delete("/{onboarding_id}")
def delete_onboarding(onboarding_id: int, db: Session = Depends(get_db)):
    db_onboarding = db.query(DBOnboarding).filter(DBOnboarding.id == onboarding_id).first()
    if db_onboarding is None:
        raise HTTPException(status_code=404, detail="Onboarding not found")
    db.delete(db_onboarding)
    db.commit()
    return {"message": "Onboarding deleted"}

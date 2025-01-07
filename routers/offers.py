from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.offer import Offer as DBOffer
from schemas.offer import Offer, OfferCreate, OfferUpdate

router = APIRouter(prefix="/offers", tags=["offers"])

@router.post("/", response_model=Offer)
def create_offer(offer: OfferCreate, db: Session = Depends(get_db)):
    new_offer = DBOffer(**offer.dict())
    db.add(new_offer)
    db.commit()
    db.refresh(new_offer)
    return new_offer

@router.get("/", response_model=list[Offer])
def read_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = db.query(DBOffer).offset(skip).limit(limit).all()
    return offers

@router.get("/{offer_id}", response_model=Offer)
def read_offer(offer_id: int, db: Session = Depends(get_db)):
    offer = db.query(DBOffer).filter(DBOffer.id == offer_id).first()
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer

@router.put("/{offer_id}", response_model=Offer)
def update_offer(offer_id: int, offer: OfferUpdate, db: Session = Depends(get_db)):
    db_offer = db.query(DBOffer).filter(DBOffer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    for key, value in offer.dict(exclude_unset=True).items():
        setattr(db_offer, key, value)
    db.commit()
    db.refresh(db_offer)
    return db_offer

@router.delete("/{offer_id}")
def delete_offer(offer_id: int, db: Session = Depends(get_db)):
    db_offer = db.query(DBOffer).filter(DBOffer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    db.delete(db_offer)
    db.commit()
    return {"message": "Offer deleted"}

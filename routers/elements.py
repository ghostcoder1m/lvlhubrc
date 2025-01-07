from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.element import Element as DBElement
from schemas.element import Element, ElementCreate, ElementUpdate

router = APIRouter(prefix="/elements", tags=["elements"])

@router.post("/", response_model=Element)
def create_element(element: ElementCreate, db: Session = Depends(get_db)):
    new_element = DBElement(**element.dict())
    db.add(new_element)
    db.commit()
    db.refresh(new_element)
    return new_element

@router.get("/", response_model=list[Element])
def read_elements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    elements = db.query(DBElement).offset(skip).limit(limit).all()
    return elements

@router.get("/{element_id}", response_model=Element)
def read_element(element_id: int, db: Session = Depends(get_db)):
    element = db.query(DBElement).filter(DBElement.id == element_id).first()
    if not element:
        raise HTTPException(status_code=404, detail="Element not found")
    return element

@router.put("/{element_id}", response_model=Element)
def update_element(element_id: int, element: ElementUpdate, db: Session = Depends(get_db)):
    db_element = db.query(DBElement).filter(DBElement.id == element_id).first()
    if db_element is None:
        raise HTTPException(status_code=404, detail="Element not found")
    for key, value in element.dict(exclude_unset=True).items():
        setattr(db_element, key, value)
    db.commit()
    db.refresh(db_element)
    return db_element

@router.delete("/{element_id}")
def delete_element(element_id: int, db: Session = Depends(get_db)):
    db_element = db.query(DBElement).filter(DBElement.id == element_id).first()
    if db_element is None:
        raise HTTPException(status_code=404, detail="Element not found")
    db.delete(db_element)
    db.commit()
    return {"message": "Element deleted"}

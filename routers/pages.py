from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.page import Page as DBPage
from schemas.page import Page, PageCreate, PageUpdate

router = APIRouter(prefix="/pages", tags=["pages"])

@router.post("/", response_model=Page)
def create_page(page: PageCreate, db: Session = Depends(get_db)):
    new_page = DBPage(**page.dict())
    db.add(new_page)
    db.commit()
    db.refresh(new_page)
    return new_page

@router.get("/", response_model=list[Page])
def read_pages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pages = db.query(DBPage).offset(skip).limit(limit).all()
    return pages

@router.get("/{page_id}", response_model=Page)
def read_page(page_id: int, db: Session = Depends(get_db)):
    page = db.query(DBPage).filter(DBPage.id == page_id).first()
    if not page:
        raise HTTPException(status_code=404, detail="Page not found")
    return page

@router.put("/{page_id}", response_model=Page)
def update_page(page_id: int, page: PageUpdate, db: Session = Depends(get_db)):
    db_page = db.query(DBPage).filter(DBPage.id == page_id).first()
    if db_page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    for key, value in page.dict(exclude_unset=True).items():
        setattr(db_page, key, value)
    db.commit()
    db.refresh(db_page)
    return db_page

@router.delete("/{page_id}")
def delete_page(page_id: int, db: Session = Depends(get_db)):
    db_page = db.query(DBPage).filter(DBPage.id == page_id).first()
    if db_page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    db.delete(db_page)
    db.commit()
    return {"message": "Page deleted"}

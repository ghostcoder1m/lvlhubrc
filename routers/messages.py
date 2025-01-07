from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.message import Message as DBMessage
from schemas.message import Message, MessageCreate, MessageUpdate

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("/", response_model=Message)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    new_message = DBMessage(**message.dict())
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message

@router.get("/", response_model=list[Message])
def read_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    messages = db.query(DBMessage).offset(skip).limit(limit).all()
    return messages

@router.get("/{message_id}", response_model=Message)
def read_message(message_id: int, db: Session = Depends(get_db)):
    message = db.query(DBMessage).filter(DBMessage.id == message_id).first()
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")
    return message

@router.put("/{message_id}", response_model=Message)
def update_message(message_id: int, message: MessageUpdate, db: Session = Depends(get_db)):
    db_message = db.query(DBMessage).filter(DBMessage.id == message_id).first()
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    for key, value in message.dict(exclude_unset=True).items():
        setattr(db_message, key, value)
    db.commit()
    db.refresh(db_message)
    return db_message

@router.delete("/{message_id}")
def delete_message(message_id: int, db: Session = Depends(get_db)):
    db_message = db.query(DBMessage).filter(DBMessage.id == message_id).first()
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    db.delete(db_message)
    db.commit()
    return {"message": "Message deleted"}

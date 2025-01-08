from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.action import Action as DBAction
from schemas.action import Action, ActionCreate, ActionUpdate

router = APIRouter(prefix="/actions", tags=["actions"])

@router.post("/", response_model=Action)
def create_action(action: ActionCreate, db: Session = Depends(get_db)):
    new_action = DBAction(**action.dict())
    db.add(new_action)
    db.commit()
    db.refresh(new_action)
    return new_action

@router.get("/", response_model=list[Action])
def get_actions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    actions = db.query(DBAction).offset(skip).limit(limit).all()
    return actions

@router.get("/{action_id}", response_model=Action)
def get_action(action_id: int, db: Session = Depends(get_db)):
    action = db.query(DBAction).filter(DBAction.id == action_id).first()
    if not action:
        raise HTTPException(status_code=404, detail="Action not found")
    return action

@router.put("/{action_id}", response_model=Action)
def update_action(action_id: int, action_update: ActionUpdate, db: Session = Depends(get_db)):
    action = db.query(DBAction).filter(DBAction.id == action_id).first()
    if not action:
        raise HTTPException(status_code=404, detail="Action not found")
    for key, value in action_update.dict(exclude_unset=True).items():
        setattr(action, key, value)
    db.commit()
    db.refresh(action)
    return action

@router.delete("/{action_id}")
def delete_action(action_id: int, db: Session = Depends(get_db)):
    action = db.query(DBAction).filter(DBAction.id == action_id).first()
    if not action:
        raise HTTPException(status_code=404, detail="Action not found")
    db.delete(action)
    db.commit()
    return {"message": "Action deleted"}

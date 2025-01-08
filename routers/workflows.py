from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.workflow import Workflow as DBWorkflow
from schemas.workflow import Workflow, WorkflowCreate, WorkflowUpdate

router = APIRouter(prefix="/workflows", tags=["workflows"])

@router.post("/", response_model=Workflow)
def create_workflow(workflow: WorkflowCreate, db: Session = Depends(get_db)):
    new_workflow = DBWorkflow(**workflow.dict())
    db.add(new_workflow)
    db.commit()
    db.refresh(new_workflow)
    return new_workflow

@router.get("/", response_model=list[Workflow])
def get_workflows(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    workflows = db.query(DBWorkflow).offset(skip).limit(limit).all()
    return workflows

@router.get("/{workflow_id}", response_model=Workflow)
def get_workflow(workflow_id: int, db: Session = Depends(get_db)):
    workflow = db.query(DBWorkflow).filter(DBWorkflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return workflow

@router.put("/{workflow_id}", response_model=Workflow)
def update_workflow(workflow_id: int, workflow_update: WorkflowUpdate, db: Session = Depends(get_db)):
    workflow = db.query(DBWorkflow).filter(DBWorkflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    for key, value in workflow_update.dict(exclude_unset=True).items():
        setattr(workflow, key, value)
    db.commit()
    db.refresh(workflow)
    return workflow

@router.delete("/{workflow_id}")
def delete_workflow(workflow_id: int, db: Session = Depends(get_db)):
    workflow = db.query(DBWorkflow).filter(DBWorkflow.id == workflow_id).first()
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
    db.delete(workflow)
    db.commit()
    return {"message": "Workflow deleted"}

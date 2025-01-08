from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class WorkflowBase(BaseModel):
    name: str
    description: Optional[str] = None
    user_id: int
    is_active: Optional[bool] = False
    is_template: Optional[bool] = False
    template_name: Optional[str] = None
    template_description: Optional[str] = None

class WorkflowCreate(WorkflowBase):
    pass

class WorkflowUpdate(WorkflowBase):
    pass

class Workflow(WorkflowBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

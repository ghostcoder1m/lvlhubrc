from pydantic import BaseModel
from typing import Optional, Dict, Any

class TriggerBase(BaseModel):
    workflow_id: int
    type: str  # e.g., 'email_opened', 'link_clicked', 'form_submitted', 'schedule'
    parameters: Optional[Dict[str, Any]] = None

class TriggerCreate(TriggerBase):
    pass

class TriggerUpdate(TriggerBase):
    pass

class Trigger(TriggerBase):
    id: int

    class Config:
        orm_mode = True

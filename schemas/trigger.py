from pydantic import BaseModel
from typing import Optional, Dict, Any

class TriggerBase(BaseModel):
    workflow_id: int
    type: str  # e.g., 'email_opened', 'link_clicked', etc.
    parameters: Optional[Dict[str, Any]] = None
    schedule: Optional[str] = None  # e.g., 'daily', 'weekly', or a CRON expression

class TriggerCreate(TriggerBase):
    pass

class TriggerUpdate(TriggerBase):
    pass

class Trigger(TriggerBase):
    id: int

    class Config:
        orm_mode = True

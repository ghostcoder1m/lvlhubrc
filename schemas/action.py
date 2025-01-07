from pydantic import BaseModel
from typing import Optional, Dict, Any

class ActionBase(BaseModel):
    trigger_id: int
    type: str  # e.g., 'send_email', 'update_lead', etc.
    parameters: Optional[Dict[str, Any]] = None
    delay_seconds: Optional[int] = 0

class ActionCreate(ActionBase):
    pass

class ActionUpdate(ActionBase):
    pass

class Action(ActionBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AutomationBase(BaseModel):
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class AutomationCreate(AutomationBase):
    pass

class AutomationUpdate(AutomationBase):
    pass

class Automation(AutomationBase):
    id: int

    class Config:
        orm_mode = True

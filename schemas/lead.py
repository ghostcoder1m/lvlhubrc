from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

class LeadBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    status: Optional[str] = "New"
    source: Optional[str] = None
    data: Optional[Dict[str, Any]] = None

class LeadCreate(LeadBase):
    owner_id: int

class LeadUpdate(LeadBase):
    pass

class Lead(LeadBase):
    id: int
    owner_id: int
    date_created: datetime

    class Config:
        orm_mode = True

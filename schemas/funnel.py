from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FunnelBase(BaseModel):
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class FunnelCreate(FunnelBase):
    pass

class FunnelUpdate(FunnelBase):
    pass

class Funnel(FunnelBase):
    id: int

    class Config:
        orm_mode = True

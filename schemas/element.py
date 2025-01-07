from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ElementBase(BaseModel):
    type: str  # e.g., 'text', 'image', 'button'
    content: str
    page_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class ElementCreate(ElementBase):
    pass

class ElementUpdate(ElementBase):
    pass

class Element(ElementBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PageBase(BaseModel):
    title: str
    content: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class PageCreate(PageBase):
    pass

class PageUpdate(PageBase):
    pass

class Page(PageBase):
    id: int

    class Config:
        orm_mode = True

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import datetime

class Element(Base):
    __tablename__ = "elements"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # e.g., 'text', 'image', 'button'
    content = Column(String)
    page_id = Column(Integer, ForeignKey("pages.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def __init__(self, type, content, page_id, created_at=None, updated_at=None):
        self.type = type
        self.content = content
        self.page_id = page_id
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self):
        return f"<Element(id={self.id}, type='{self.type}', created_at='{self.created_at}', updated_at='{self.updated_at}')>"

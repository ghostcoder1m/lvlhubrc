from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="workflows")
    triggers = relationship("Trigger", back_populates="workflow")
    actions = relationship("Action", back_populates="workflow")

    def __init__(self, name, description, user_id, is_active=False, created_at=None, updated_at=None):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def __repr__(self):
        return f"<Workflow(id={self.id}, name='{self.name}', user_id={self.user_id}, is_active={self.is_active}, created_at='{self.created_at}', updated_at='{self.updated_at}')>"

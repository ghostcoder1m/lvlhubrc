from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Automation(Base):
    __tablename__ = "automations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    description = Column(String)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="automations")

    def __init__(self, user_id, name, description, is_active=True):
        self.user_id = user_id
        self.name = name
        self.description = description
        self.is_active = is_active

    def __repr__(self):
        return f"<Automation(id={self.id}, user_id={self.user_id}, name='{self.name}', is_active={self.is_active})>"

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
    is_template = Column(Boolean, default=False)
    template_name = Column(String, nullable=True)
    template_description = Column(String, nullable=True)
    version = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="workflows")

    def __init__(self, name, description, user_id, is_active=False, is_template=False, template_name=None, template_description=None):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.is_active = is_active
        self.is_template = is_template
        self.template_name = template_name
        self.template_description = template_description

    def __repr__(self):
        return f"<Workflow(id={self.id}, name='{self.name}', description='{self.description}', user_id={self.user_id}, is_active={self.is_active}, is_template={self.is_template})>"

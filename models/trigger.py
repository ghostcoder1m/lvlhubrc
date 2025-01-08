from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base

class Trigger(Base):
    __tablename__ = "triggers"

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey("workflows.id"))
    type = Column(String)  # e.g., 'email_opened', 'link_clicked', 'form_submitted', 'schedule'
    parameters = Column(JSON)  # Store any trigger-specific parameters

    workflow = relationship("Workflow", back_populates="triggers")
    actions = relationship("Action", back_populates="trigger")

    def __init__(self, workflow_id, type, parameters):
        self.workflow_id = workflow_id
        self.type = type
        self.parameters = parameters

    def __repr__(self):
        return f"<Trigger(id={self.id}, workflow_id={self.workflow_id}, type='{self.type}')>"

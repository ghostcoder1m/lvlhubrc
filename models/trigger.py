from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from database import Base

class Trigger(Base):
    __tablename__ = "triggers"

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey("workflows.id"))
    type = Column(String)  # e.g., 'email_opened', 'link_clicked', 'form_submitted', etc.
    parameters = Column(JSON)  # Store any trigger-specific parameters
    schedule = Column(String, nullable=True)  # e.g., 'daily', 'weekly', or a CRON expression

    def __init__(self, workflow_id, type, parameters, schedule=None):
        self.workflow_id = workflow_id
        self.type = type
        self.parameters = parameters
        self.schedule = schedule

    def __repr__(self):
        return f"<Trigger(id={self.id}, type='{self.type}', workflow_id={self.workflow_id}, schedule='{self.schedule}')>"

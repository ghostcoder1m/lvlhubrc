from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from database import Base

class Action(Base):
    __tablename__ = "actions"

    id = Column(Integer, primary_key=True, index=True)
    trigger_id = Column(Integer, ForeignKey("triggers.id"))
    type = Column(String)  # e.g., 'send_email', 'update_lead', etc.
    parameters = Column(JSON)  # Store action-specific parameters
    delay_seconds = Column(Integer, default=0)

    def __init__(self, trigger_id, type, parameters, delay_seconds=0):
        self.trigger_id = trigger_id
        self.type = type
        self.parameters = parameters
        self.delay_seconds = delay_seconds

    def __repr__(self):
        return f"<Action(id={self.id}, type='{self.type}', trigger_id={self.trigger_id}, delay_seconds={self.delay_seconds})>"

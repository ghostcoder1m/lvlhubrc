from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from database import Base
from datetime import datetime

class ActionExecution(Base):
    __tablename__ = "action_executions"

    id = Column(Integer, primary_key=True, index=True)
    workflow_execution_id = Column(Integer, ForeignKey("workflow_executions.id"))
    action_id = Column(Integer, ForeignKey("actions.id"))
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    status = Column(String)  # e.g., 'running', 'completed', 'failed'
    result = Column(String, nullable=True)  # For storing action execution output, errors, or other details.

    def __init__(self, workflow_execution_id, action_id, start_time=None, end_time=None, status='running', result=None):
        self.workflow_execution_id = workflow_execution_id
        self.action_id = action_id
        self.start_time = start_time or datetime.utcnow()
        self.end_time = end_time
        self.status = status
        self.result = result

    def __repr__(self):
        return f"<ActionExecution(id={self.id}, workflow_execution_id={self.workflow_execution_id}, action_id={self.action_id}, start_time='{self.start_time}', end_time='{self.end_time}', status='{self.status}')>"

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Onboarding(Base):
    __tablename__ = "onboardings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String)  # e.g., 'in_progress', 'completed'
    steps_completed = Column(Integer, default=0)

    user = relationship("User", back_populates="onboarding")

    def __init__(self, user_id, status, steps_completed=0):
        self.user_id = user_id
        self.status = status
        self.steps_completed = steps_completed

    def __repr__(self):
        return f"<Onboarding(id={self.id}, user_id={self.user_id}, status='{self.status}', steps_completed={self.steps_completed})>"

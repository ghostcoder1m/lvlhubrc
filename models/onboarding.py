from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Onboarding(Base):
    __tablename__ = "onboardings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String)  # e.g., 'completed', 'in_progress'

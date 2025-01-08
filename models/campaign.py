from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="campaigns")

    def __init__(self, name, description, user_id, start_date=None, end_date=None):
        self.name = name
        self.description = description
        self.user_id = user_id
        self.start_date = start_date or datetime.utcnow()
        self.end_date = end_date

    def __repr__(self):
        return f"<Campaign(id={self.id}, name='{self.name}', description='{self.description}', start_date='{self.start_date}', end_date='{self.end_date}', user_id={self.user_id})>"

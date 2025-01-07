from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from database import Base
from datetime import datetime

class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    discount_percentage = Column(Float)
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

    def __init__(self, name, description, discount_percentage, start_date=None, end_date=None):
        self.name = name
        self.description = description
        self.discount_percentage = discount_percentage
        self.start_date = start_date or datetime.utcnow()
        self.end_date = end_date

    def __repr__(self):
        return f"<Offer(id={self.id}, name='{self.name}', description='{self.description}', discount_percentage={self.discount_percentage}, start_date='{self.start_date}', end_date='{self.end_date}')>"

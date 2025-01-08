from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    status = Column(String)  # e.g., 'New', 'Contacted', 'Qualified', 'Lost', 'Converted'
    source = Column(String)  # e.g., 'Web Form', 'Advertisement', 'Referral'
    owner_id = Column(Integer, ForeignKey("users.id"))
    date_created = Column(DateTime, default=datetime.utcnow)
    data = Column(JSON)  # To store extra information gathered from integrations.

    owner = relationship("User", back_populates="leads")

    def __init__(self, first_name, last_name, email, phone, status, source, owner_id, date_created=None, data=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.status = status
        self.source = source
        self.owner_id = owner_id
        self.date_created = date_created or datetime.utcnow()
        self.data = data

    def __repr__(self):
        return f"<Lead(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}', phone='{self.phone}', status='{self.status}', source='{self.source}', owner_id={self.owner_id}, date_created='{self.date_created}')>"

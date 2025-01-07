from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from datetime import datetime

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, ForeignKey("users.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __init__(self, content, sender_id, recipient_id, timestamp=None):
        self.content = content
        self.sender_id = sender_id
        self.recipient_id = recipient_id
        self.timestamp = timestamp or datetime.utcnow()

    def __repr__(self):
        return f"<Message(id={self.id}, content='{self.content}', sender_id={self.sender_id}, recipient_id={self.recipient_id}, timestamp='{self.timestamp}')>"

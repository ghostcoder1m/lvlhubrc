from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(prefix="/events", tags=["events"])

@router.post("/")
def track_event(event_data: dict, db: Session = Depends(get_db)):
    """Track an event."""
    # Here you would implement logic to save the event data to the database
    return {"message": "Event tracked successfully", "data": event_data}

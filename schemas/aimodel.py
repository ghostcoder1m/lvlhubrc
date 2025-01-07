from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AIModelBase(BaseModel):
    name: str  # e.g., "lead_scoring_model", "recommendation_model"
    version: int
    description: Optional[str] = None
    model_type: str  # e.g., "logistic_regression", "random_forest"
    filepath: str  # Path to the serialized model file
    created_at: Optional[datetime] = None
    is_active: Optional[bool] = True  # Indicates whether this version is currently active

class AIModelCreate(AIModelBase):
    pass

class AIModelUpdate(AIModelBase):
    pass

class AIModel(AIModelBase):
    id: int

    class Config:
        orm_mode = True

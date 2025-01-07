from pydantic import BaseModel
from typing import Optional

class OnboardingBase(BaseModel):
    user_id: int
    status: str  # e.g., 'completed', 'in_progress'

class OnboardingCreate(OnboardingBase):
    pass

class OnboardingUpdate(OnboardingBase):
    pass

class Onboarding(OnboardingBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel, EmailStr

class SignupForm(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str

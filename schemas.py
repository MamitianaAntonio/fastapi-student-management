from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class StudentCreate(BaseModel):
    firstName: str
    lastName: str
    email: EmailStr
    grade: float
    isActive: bool = True


class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    grade: Optional[float] = None
    is_active: Optional[bool] = None


class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    grade: float
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

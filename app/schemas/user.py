from pydantic import BaseModel, ConfigDict
from datetime import date
from app.models.enums import Role
from typing import Optional

class UserCreate(BaseModel):
    name: str
    date_of_baptism: date | None
    group_id: int
    phone: str

class UserResponse(BaseModel):
    id: int
    name: str
    date_of_baptism: date | None
    group_id: int
    phone: str
    model_config=ConfigDict(from_attributes=True)

from pydantic import BaseModel
from pydantic import EmailStr


class StudentCreate(BaseModel):
    name: str
    email: EmailStr


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
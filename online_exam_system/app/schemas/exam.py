from pydantic import BaseModel, Field


class ExamCreate(BaseModel):
    title: str
    category: str
    duration: int = Field(gt=0)
    is_active: bool = True
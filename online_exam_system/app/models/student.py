from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    attempts = relationship(
        "ExamAttempt",
        back_populates="student"
    )
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database import Base


class ExamAttempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    exam_id = Column(
        Integer,
        ForeignKey("exams.id")
    )

    score = Column(Integer, default=0)

    status = Column(String)

    student = relationship(
        "Student",
        back_populates="attempts"
    )

    exam = relationship(
        "Exam",
        back_populates="attempts"
    )
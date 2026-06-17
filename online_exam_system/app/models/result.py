from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey

from app.database import Base


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id")
    )

    exam_id = Column(
        Integer,
        ForeignKey("exams.id")
    )

    score = Column(Integer)

    
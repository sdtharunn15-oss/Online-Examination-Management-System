from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)

    exam_id = Column(
        Integer,
        ForeignKey("exams.id")
    )

    question_text = Column(String)

    option_a = Column(String)

    option_b = Column(String)

    option_c = Column(String)

    option_d = Column(String)

    correct_answer = Column(String)

    exam = relationship(
        "Exam",
        back_populates="questions"
    )
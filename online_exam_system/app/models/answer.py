from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)

    attempt_id = Column(
        Integer,
        ForeignKey("attempts.id")
    )

    question_id = Column(
        Integer,
        ForeignKey("questions.id")
    )

    selected_answer = Column(String)
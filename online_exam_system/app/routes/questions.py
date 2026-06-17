from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.exam import Exam
from app.models.question import Question

from app.schemas.question import QuestionCreate

from app.dependencies import admin_required

router = APIRouter(
    prefix="/api/v1/questions",
    tags=["Questions"]
)

@router.post("/")
def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db)
):
    exam = db.query(Exam).filter(
        Exam.id == question.exam_id
    ).first()

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )


    if question.correct_answer not in ["A", "B", "C", "D"]:
        raise HTTPException(
            status_code=400,
            detail="Correct answer must be A/B/C/D"
        )

    new_question = Question(
        exam_id=question.exam_id,
        question_text=question.question_text,
        option_a=question.option_a,
        option_b=question.option_b,
        option_c=question.option_c,
        option_d=question.option_d,
        correct_answer=question.correct_answer
    )

    db.add(new_question)
    db.commit()
    db.refresh(new_question)

    return new_question


@router.get("/exam/{exam_id}")
def get_exam_questions(
    exam_id: int,
    db: Session = Depends(get_db)
):

    exam = db.query(Exam).filter(
        Exam.id == exam_id
    ).first()

    if not exam:
        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )

    return db.query(Question).filter(
        Question.exam_id == exam_id
    ).all()



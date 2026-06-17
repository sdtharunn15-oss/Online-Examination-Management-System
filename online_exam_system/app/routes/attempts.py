from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session

from app.database import get_db

from app.services.email_service import send_email

from app.models.student import Student
from app.models.exam import Exam
from app.models.question import Question
from app.models.attempt import ExamAttempt
from app.models.answer import Answer
from app.models.result import Result

from app.schemas.attempt import (
    StartAttempt,
    SubmitAttempt
)


router = APIRouter(
    prefix="/api/v1/attempts",
    tags=["Attempts"]
)


@router.post("/start")
def start_exam(
    data: StartAttempt,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == data.student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )


    exam = db.query(Exam).filter(
        Exam.id == data.exam_id
    ).first()


    if not exam:
        raise HTTPException(
            status_code=404,
            detail="Exam not found"
        )


    if not exam.is_active:
        raise HTTPException(
            status_code=400,
            detail="Exam inactive"
        )


    existing = db.query(ExamAttempt).filter(
        ExamAttempt.student_id == data.student_id,
        ExamAttempt.exam_id == data.exam_id
    ).first()


    if existing:
        raise HTTPException(
            status_code=400,
            detail="Student already attempted this exam"
        )


    attempt = ExamAttempt(
        student_id=data.student_id,
        exam_id=data.exam_id,
        status="Started",
        score=0
    )


    db.add(attempt)
    db.commit()
    db.refresh(attempt)


    return attempt




@router.post("/submit")
def submit_exam(
    data: SubmitAttempt,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):


    attempt = db.query(ExamAttempt).filter(
        ExamAttempt.id == data.attempt_id
    ).first()


    if not attempt:
        raise HTTPException(
            status_code=404,
            detail="Attempt not found"
        )


    if attempt.status == "Completed":

        raise HTTPException(
            status_code=400,
            detail="Already submitted"
        )



    score = 0



    for ans in data.answers:


        question = db.query(Question).filter(
            Question.id == ans.question_id
        ).first()



        if question is None:

            raise HTTPException(
                status_code=404,
                detail=f"Question {ans.question_id} not found"
            )



        if question.correct_answer == ans.answer:

            score += 1



        answer = Answer(

            attempt_id = attempt.id,

            question_id = ans.question_id,

            selected_answer = ans.answer

        )


        db.add(answer)



    attempt.score = score

    attempt.status = "Completed"



    result = Result(

        student_id = attempt.student_id,

        exam_id = attempt.exam_id,

        score = score

    )


    db.add(result)


    db.commit()



    student = db.query(Student).filter(
        Student.id == attempt.student_id
    ).first()



    if student:

        background_tasks.add_task(
            send_email,
            student.email,
            score
        )



    return {

        "message": "Exam submitted successfully",

        "score": score,

        "status": "Completed"

    }






@router.get("/{attempt_id}")
def get_attempt(

    attempt_id:int,

    db:Session = Depends(get_db)

):


    attempt = db.query(ExamAttempt).filter(
        ExamAttempt.id == attempt_id
    ).first()



    if not attempt:

        raise HTTPException(

            status_code=404,

            detail="Attempt not found"

        )


    return attempt
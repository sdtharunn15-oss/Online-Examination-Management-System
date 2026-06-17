from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.exam import Exam
from app.schemas.exam import ExamCreate
from app.dependencies import admin_required

router = APIRouter(
    prefix="/api/v1/exams",
    tags=["Exams"]
)

@router.post("/")
def create_exam(
    exam: ExamCreate,
    db: Session = Depends(get_db)
):
    if exam.duration <= 0:
        raise HTTPException(
            status_code=400,
            detail="Duration must be greater than 0"
        )

    new_exam = Exam(
        title=exam.title,
        category=exam.category,
        duration=exam.duration,
        is_active=exam.is_active
    )

    db.add(new_exam)
    db.commit()
    db.refresh(new_exam)

    return new_exam

@router.get("/")
def get_exams(
    category: str = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Exam)

    if category:
        query = query.filter(
            Exam.category == category
        )

    offset = (page - 1) * limit

    return query.offset(offset)\
        .limit(limit)\
        .all()

   
   


@router.get("/{exam_id}")
def get_exam(
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

    return exam



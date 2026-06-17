from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.student import Student
from app.models.attempt import ExamAttempt

from app.schemas.student import StudentCreate

from app.dependencies import admin_required

router = APIRouter(
    prefix="/api/v1/students",
    tags=["Students"]
)

@router.post("/")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    
    existing = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_student = Student(
        name=student.name,
        email=student.email
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return new_student

@router.get("/")
def get_students(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    offset = (page - 1) * limit

    return db.query(Student)\
        .offset(offset)\
        .limit(limit)\
        .all()
    

@router.get("/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):

    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

@router.get("/{student_id}/exams")
def student_exam_history(
    student_id: int,
    db: Session = Depends(get_db)
):

    attempts = db.query(
        ExamAttempt
    ).filter(
        ExamAttempt.student_id == student_id
    ).all()

    return attempts


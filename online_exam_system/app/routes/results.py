from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.result import Result
from app.models.student import Student

router = APIRouter(
    prefix="/api/v1/results",
    tags=["Results"]
)


@router.get("/")
def get_results(
    student_id: int = None,
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(Result)

    if student_id:
        query = query.filter(
            Result.student_id == student_id
        )

    offset = (page - 1) * limit

    return query.offset(offset)\
        .limit(limit)\
        .all()


@router.get("/leaderboard")
def leaderboard(
    db: Session = Depends(get_db)
):
    results = db.query(Result)\
        .order_by(Result.score.desc())\
        .all()

    leaderboard = []

    rank = 1

    for result in results:

        student = db.query(Student).filter(
            Student.id == result.student_id
        ).first()

        leaderboard.append({
            "rank": rank,
            "student": student.name,
            "score": result.score
        })

        rank += 1

    return leaderboard
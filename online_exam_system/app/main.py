from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

# import models so tables are created
from app.models.user import User
from app.models.student import Student
from app.models.exam import Exam
from app.models.question import Question
from app.models.attempt import ExamAttempt
from app.models.result import Result


# Import routers
from app.routes.auth import router as auth_router
from app.routes.students import router as student_router
from app.routes.exams import router as exam_router
from app.routes.questions import router as question_router
from app.routes.attempts import router as attempt_router
from app.routes.results import router as result_router


# Create tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Online Examination Management System",
    version="1.0.0"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register routes
app.include_router(auth_router)

app.include_router(student_router)

app.include_router(exam_router)

app.include_router(question_router)

app.include_router(attempt_router)

app.include_router(result_router)



@app.get("/")
def home():
    return {
        "message": "Online Examination System Running"
    }